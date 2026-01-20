"""CLI entry point for A12 Widget documentation retrieval."""

import json
import logging
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

from .crawler import BASE_URL, crawl_page, get_version, download_image, wait_for_content, extract_links, normalize_hash_path, discover_urls_via_search
from .extractor import extract_content, transform_links, update_image_references
from .storage import hash_path_to_directory, save_markdown, save_image

# Module-level logger
logger = logging.getLogger(__name__)


def setup_logging(output_dir: Path) -> None:
    """Setup logging to pages.log file."""
    log_file = output_dir / 'pages.log'

    # Configure file handler
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

    # Add to logger
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)


def load_state(output_dir: Path) -> dict:
    """Load state from pages.json or create a new state.

    Returns state dict. If file doesn't exist, creates new state.
    If file is corrupted, logs warning and creates new state.
    """
    state_file = output_dir / 'pages.json'

    if state_file.exists():
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)
            # Validate structure
            if 'scrape' in state and 'pages' in state:
                return state
            print('Warning: Invalid state file structure, starting fresh', file=sys.stderr)
        except json.JSONDecodeError:
            print('Warning: Corrupted state file, starting fresh', file=sys.stderr)

    # Create new state
    return {
        'scrape': {
            'scrape_started': None,
            'scrape_finished': None
        },
        'pages': []
    }


def save_state(output_dir: Path, state: dict) -> None:
    """Save state to pages.json atomically (temp file + rename)."""
    state_file = output_dir / 'pages.json'

    # Write to temp file first
    fd, temp_path = tempfile.mkstemp(dir=output_dir, suffix='.json')
    try:
        with open(fd, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)
        # Atomic rename
        Path(temp_path).replace(state_file)
    except Exception:
        # Clean up temp file on error
        Path(temp_path).unlink(missing_ok=True)
        raise


def add_page(state: dict, url: str) -> bool:
    """Add a new URL to state if not already present.

    Returns True if URL was added, False if already exists.
    Normalizes URLs by stripping section anchors.
    """
    # Handle home page specially
    if url == '#/':
        normalized = '#/'
    else:
        # Normalize URL (strip section anchors)
        normalized = normalize_hash_path(url)
        if not normalized:
            return False

    # Check if URL already exists
    for page in state['pages']:
        if page['url'] == normalized:
            return False

    # Add new page entry
    state['pages'].append({
        'url': normalized,
        'scrape_started': None,
        'scrape_finished': None,
        'scrape_result': None,
        'scrape_error': None
    })
    return True


def update_page_status(state: dict, url: str, result: str, error: str = None) -> None:
    """Update page scrape status.

    Args:
        state: State dict
        url: Page URL
        result: 'in_progress', 'success', or 'error'
        error: Error message if result is 'error'
    """
    for page in state['pages']:
        if page['url'] == url:
            now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

            if result == 'in_progress':
                page['scrape_started'] = now
                page['scrape_finished'] = None
                page['scrape_result'] = 'in_progress'
                page['scrape_error'] = None
            elif result == 'success':
                page['scrape_finished'] = now
                page['scrape_result'] = 'success'
                page['scrape_error'] = None
            elif result == 'error':
                page['scrape_finished'] = now
                page['scrape_result'] = 'error'
                page['scrape_error'] = error
            return


def get_next_pending_page(state: dict) -> str | None:
    """Get the next page URL that needs to be scraped.

    Returns URL or None if all pages are complete.
    Skips pages that are already 'success' or 'error'.
    """
    for page in state['pages']:
        if page['scrape_result'] not in ('success', 'error'):
            return page['url']
    return None


def get_progress_counts(state: dict) -> tuple[int, int]:
    """Get (completed, total) page counts."""
    completed = sum(1 for p in state['pages'] if p['scrape_result'] == 'success')
    total = len(state['pages'])
    return completed, total


def format_progress_bar(completed: int, total: int, current_url: str = None, width: int = 20) -> str:
    """Format a progress bar string."""
    if total == 0:
        pct = 0
        filled = 0
    else:
        pct = (completed / total) * 100
        filled = int((completed / total) * width)

    bar = '█' * filled + '░' * (width - filled)

    if current_url:
        # Truncate URL if too long for display
        max_url_len = 50
        display_url = current_url if len(current_url) <= max_url_len else current_url[:max_url_len-3] + '...'
        return f'Scraping: [{bar}] {completed:3}/{total:<3} ({pct:3.0f}%) - {display_url}'
    else:
        return f'Scraping: [{bar}] {completed:3}/{total:<3} ({pct:3.0f}%)'


def print_progress(msg: str) -> None:
    """Print progress message, clearing the line first."""
    # Clear line and print
    print(f'\r\033[K{msg}', end='', file=sys.stderr, flush=True)


def main():
    """Main entry point."""
    print('Starting A12 Widget documentation retrieval...', file=sys.stderr)

    with sync_playwright() as p:
        print('Launching browser...', file=sys.stderr)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1400, 'height': 900})
        print('Browser launched, navigating to site...', file=sys.stderr)

        # Navigate to site and get version
        page.goto(BASE_URL + '#/')
        print('Waiting for content...', file=sys.stderr)
        wait_for_content(page)
        print('Content loaded.', file=sys.stderr)

        version = get_version(page)
        print(f'Detected version: {version}', file=sys.stderr)

        # Create output directory
        output_dir = Path(f'A12_Widget_Documentation_{version}')
        output_dir.mkdir(exist_ok=True)
        print(f'Output directory: {output_dir}', file=sys.stderr)

        # Setup logging
        setup_logging(output_dir)
        logger.info('='*60)
        logger.info(f'Starting scrape session, version: {version}')

        # Load or create state
        state = load_state(output_dir)

        # Determine if this is a fresh start, resume, or re-scrape
        is_resume = False
        if state['scrape']['scrape_started']:
            if state['scrape']['scrape_finished']:
                # Previous scrape finished - this is a re-scrape
                print('Previous scrape completed. Starting re-scrape...', file=sys.stderr)
                logger.info('Previous scrape completed. Starting re-scrape.')
                state['scrape']['scrape_finished'] = None
            else:
                # Previous scrape was interrupted - resume
                is_resume = True
                completed, total = get_progress_counts(state)
                print(f'Resuming: {completed}/{total} pages already completed', file=sys.stderr)
                logger.info(f'Resuming interrupted scrape: {completed}/{total} pages completed')
        else:
            logger.info('Fresh start - no previous state')

        # Set scrape start time
        state['scrape']['scrape_started'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

        # Reset any in_progress or error pages (they should be retried)
        for page_entry in state['pages']:
            if page_entry['scrape_result'] in ('in_progress', 'error'):
                logger.info(f'Resetting {page_entry["scrape_result"]} page for retry: {page_entry["url"]}')
                page_entry['scrape_result'] = None
                page_entry['scrape_started'] = None
                page_entry['scrape_finished'] = None
                page_entry['scrape_error'] = None

        # Add start URL
        add_page(state, '#/')

        # Discover all URLs via search dialog
        print('Discovering all pages via search dialog...', file=sys.stderr)
        logger.info('Starting URL discovery via search dialog')
        discovered_urls = discover_urls_via_search(page)
        added_count = 0
        for url in discovered_urls:
            if add_page(state, url):
                added_count += 1
        print(f'Discovered {len(discovered_urls)} URLs ({added_count} new)', file=sys.stderr)
        logger.info(f'Discovered {len(discovered_urls)} URLs via search dialog ({added_count} new)')

        save_state(output_dir, state)

        # Track timing
        start_time = time.time()

        # Unified scrape loop
        success_count = 0
        error_count = 0

        while True:
            # Get next pending page
            hash_path = get_next_pending_page(state)
            if hash_path is None:
                break

            # Update progress display
            completed, total = get_progress_counts(state)
            progress = format_progress_bar(completed, total, hash_path)
            print_progress(progress)

            # Mark as in progress
            update_page_status(state, hash_path, 'in_progress')
            save_state(output_dir, state)
            logger.info(f'Starting crawl: {hash_path}')

            # Crawl the page
            content = crawl_page(page, hash_path)

            # Extract links FIRST (even if content crawl failed)
            # This ensures we discover URLs even from pages that timeout
            logger.debug(f'Extracting links from: {hash_path}')
            new_urls = extract_links(page)
            added_count = 0
            for url in new_urls:
                if add_page(state, url):
                    added_count += 1
                    logger.debug(f'Discovered new URL: {url}')
            if added_count > 0:
                logger.info(f'Discovered {added_count} new URLs from {hash_path}')
                save_state(output_dir, state)

            if content is None:
                update_page_status(state, hash_path, 'error', 'Failed to crawl page')
                save_state(output_dir, state)
                error_count += 1
                logger.error(f'Failed to crawl: {hash_path}')
                continue

            logger.debug(f'Crawled successfully: {hash_path}, title: {content.title}')

            # Extract markdown and images
            extracted = extract_content(content.html, BASE_URL, hash_path)

            # Get directory name
            dir_name = hash_path_to_directory(hash_path)

            # Download images and build URL -> filename mapping
            url_to_filename = {}
            for idx, img_url in enumerate(extracted.image_urls, 1):
                img_data = download_image(page, img_url)
                if img_data:
                    filename = save_image(output_dir, dir_name, img_data, img_url, idx)
                    url_to_filename[img_url] = filename

            # Transform links and image references
            markdown = transform_links(extracted.markdown, dir_name, BASE_URL)
            markdown = update_image_references(markdown, url_to_filename)

            # Add title as H1 if not present
            if not markdown.startswith('# '):
                title = content.title.replace(' | mgm A12', '').strip()
                if title:
                    markdown = f'# {title}\n\n{markdown}'

            # Save markdown
            save_markdown(output_dir, dir_name, markdown)

            # Mark as success
            update_page_status(state, hash_path, 'success')
            save_state(output_dir, state)
            success_count += 1
            logger.info(f'Completed: {hash_path} ({success_count} done, {len(state["pages"])} total)')

        # Mark scrape as finished
        logger.info(f'Scrape loop finished: {success_count} success, {error_count} errors')
        state['scrape']['scrape_finished'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        save_state(output_dir, state)

        browser.close()

    # Final progress display
    completed, total = get_progress_counts(state)
    progress = format_progress_bar(completed, total)
    print(f'\r\033[K{progress}', file=sys.stderr)

    # Calculate duration
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    duration = f'{minutes}m {seconds}s' if minutes > 0 else f'{seconds}s'

    print(f'Done! Scraped {success_count} pages in {duration}', file=sys.stderr)
    if error_count > 0:
        print(f'({error_count} errors)', file=sys.stderr)
    print(f'Output: {output_dir}/', file=sys.stderr)


if __name__ == '__main__':
    main()
