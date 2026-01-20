"""Playwright navigation and URL discovery."""

import sys
import time
from dataclasses import dataclass

from playwright.sync_api import Page, sync_playwright, TimeoutError as PlaywrightTimeout


BASE_URL = 'https://www.mgm-tp.com/a12.htmlshowcase/'


@dataclass
class PageContent:
    """Content extracted from a page."""
    url: str
    hash_path: str
    html: str
    title: str


def wait_for_content(page: Page, timeout: int = 30000) -> bool:
    """Wait for content to be fully rendered.

    Returns True if content is ready, False if timeout.
    """
    try:
        # Wait for main element with substantial content
        page.locator('[role="main"]').first.wait_for(state='visible', timeout=timeout)
        # Give time for content to render
        time.sleep(0.5)
        return True
    except PlaywrightTimeout:
        return False


def get_version(page: Page) -> str:
    """Extract version from page header."""
    try:
        # Version is displayed as text like "38.1.1" in the banner
        banner = page.locator('[role="banner"]')
        text = banner.inner_text(timeout=5000)
        import re
        match = re.search(r'(\d+\.\d+\.\d+)', text)
        if match:
            return match.group(1)
        return 'unknown'
    except Exception:
        return 'unknown'


def discover_urls_via_search(page: Page) -> list[str]:
    """Discover all content URLs by traversing all navigation sections.

    The sidebar uses accordion behavior (only one category expanded at a time),
    so we must process each category separately and handle nested categories.

    Returns list of hash paths (e.g., ['#/get-started/quick-start', ...])
    """
    discovered = set()

    # Main navigation sections to visit
    sections = [
        ('Get Started', '#/get-started'),
        ('Basics', '#/basics'),
        ('Widgets', '#/widgets'),
        ('Experimental', '#/experimental'),
        ('Examples', '#/examples'),
        ('FAQ', '#/faq'),
    ]

    def collect_urls_from_section(p: Page, section_hash: str) -> set[str]:
        """Collect all URLs from a section by expanding each category."""
        urls = set()

        # Use JavaScript to systematically click through all items
        result = p.evaluate('''async (sectionHash) => {
            const discovered = new Set();
            const processedCategories = new Set();

            async function wait(ms) {
                return new Promise(r => setTimeout(r, ms));
            }

            async function processCurrentView() {
                // Get all sidebar buttons
                const buttons = Array.from(document.querySelectorAll('[role="button"]'));
                const sidebarBtns = buttons.filter(btn => {
                    const rect = btn.getBoundingClientRect();
                    return rect.x < 400 && rect.width > 0;
                });

                // Find categories (buttons ending with add/remove)
                const categories = sidebarBtns.filter(btn => {
                    const text = btn.textContent || '';
                    return (text.endsWith('add') || text.endsWith('remove')) &&
                           !text.includes('Show App');
                });

                // Find leaf items (no add/remove)
                const leaves = sidebarBtns.filter(btn => {
                    const text = (btn.textContent || '').trim();
                    return !text.endsWith('add') && !text.endsWith('remove') &&
                           !text.includes('Theme') && !text.includes('Show App') &&
                           text.length > 0 && text.length < 100;
                });

                // Click each leaf and capture URL
                for (const leaf of leaves) {
                    try {
                        leaf.click();
                        await wait(80);
                        const hash = window.location.hash;
                        if (hash && hash !== '#/' && hash.length > 3) {
                            discovered.add(hash);
                        }
                    } catch (e) {}
                }

                // Return list of collapsed categories to process
                return categories
                    .filter(btn => btn.textContent.endsWith('add'))
                    .map(btn => btn.textContent.replace(/add$/, '').trim())
                    .filter(name => !processedCategories.has(name));
            }

            // Initial processing
            let categoriesToExpand = await processCurrentView();

            // Process each category
            while (categoriesToExpand.length > 0) {
                const catName = categoriesToExpand.shift();
                processedCategories.add(catName);

                // Find and click this category to expand it
                const buttons = Array.from(document.querySelectorAll('[role="button"]'));
                const catBtn = buttons.find(btn => {
                    const rect = btn.getBoundingClientRect();
                    if (rect.x >= 400 || rect.width === 0) return false;
                    const text = btn.textContent || '';
                    return text.endsWith('add') && text.replace(/add$/, '').trim() === catName;
                });

                if (catBtn) {
                    catBtn.click();
                    await wait(150);

                    // Process the newly expanded category
                    const newCategories = await processCurrentView();
                    for (const nc of newCategories) {
                        if (!processedCategories.has(nc)) {
                            categoriesToExpand.push(nc);
                        }
                    }
                }
            }

            return Array.from(discovered);
        }''', section_hash)

        for url in result:
            normalized = normalize_hash_path(url)
            if normalized:
                urls.add(normalized)

        return urls

    for section_name, section_hash in sections:
        print(f'Discovering URLs in section: {section_name}', file=sys.stderr)

        # Navigate to section
        page.goto(BASE_URL + section_hash)
        wait_for_content(page, timeout=10000)
        time.sleep(0.3)

        # Collect all URLs from this section
        section_urls = collect_urls_from_section(page, section_hash)
        new_urls = section_urls - discovered
        discovered.update(section_urls)

        print(f'  Found {len(new_urls)} URLs in {section_name} ({len(discovered)} total)', file=sys.stderr)

    print(f'Discovered {len(discovered)} total URLs', file=sys.stderr)
    return sorted(list(discovered))


def discover_urls(page: Page) -> list[str]:
    """Discover all content URLs by traversing navigation.

    Returns list of hash paths (e.g., ['#/get-started/quick-start', ...])
    """
    discovered = set()

    def expand_all_side_nav():
        """Expand all collapsed side navigation items."""
        max_iterations = 100
        iteration = 0

        while iteration < max_iterations:
            iteration += 1
            # Find buttons with 'add' icon (collapsed state) using Playwright locators
            # These are buttons that contain text 'add' which is the expand icon
            try:
                collapsed = page.get_by_role('button').filter(has_text='add').all()

                if not collapsed:
                    break

                found_any = False
                for btn in collapsed:
                    try:
                        # Only click if it's a navigation expand button (has 'add' as icon text)
                        btn_text = btn.inner_text(timeout=1000)
                        if '\nadd' in btn_text or btn_text.endswith('add'):
                            if btn.is_visible():
                                btn.click()
                                time.sleep(0.3)
                                found_any = True
                    except Exception:
                        continue

                if not found_any:
                    break

            except Exception:
                break

    def collect_leaf_urls():
        """Collect URLs from leaf navigation items."""
        # Get all buttons that could be navigation items
        buttons = page.get_by_role('button').all()

        for btn in buttons:
            try:
                if not btn.is_visible():
                    continue

                btn_text = btn.inner_text(timeout=500)

                # Skip buttons with expand/collapse icons (add/remove)
                if '\nadd' in btn_text or btn_text.endswith('add'):
                    continue
                if '\nremove' in btn_text or btn_text.endswith('remove'):
                    continue

                # Skip theme selector and other non-nav buttons
                if 'Theme Selector' in btn_text or 'EXPLORE' in btn_text or 'TAKE A LOOK' in btn_text:
                    continue

                # This looks like a leaf navigation button - click it
                btn.click()
                time.sleep(0.3)

                # Collect the hash
                current_hash = page.evaluate('() => window.location.hash')
                if current_hash and current_hash != '#/' and current_hash not in discovered:
                    discovered.add(current_hash)

            except Exception:
                continue

    # Navigate to base URL
    page.goto(BASE_URL + '#/')
    wait_for_content(page)

    # Get top navigation items using role-based locators
    # The top nav items are links inside the main navigation
    main_nav = page.locator('[aria-label="Main navigation"]')
    top_nav_items = main_nav.get_by_role('link').all()

    nav_texts = []
    for item in top_nav_items:
        try:
            text = item.inner_text(timeout=1000)
            if text.strip():
                nav_texts.append(text.strip())
        except Exception:
            continue

    print(f'Found {len(nav_texts)} top nav items: {nav_texts}', file=sys.stderr)

    # Process each top nav section
    for nav_text in nav_texts:
        try:
            print(f'Processing section: {nav_text}', file=sys.stderr)

            # Handle overflow menu (icon text is "more_horiz" but link name is "Further menuitems")
            if nav_text == 'more_horiz':
                nav_item = main_nav.get_by_role('link', name='Further menuitems')
            else:
                nav_item = main_nav.get_by_role('link', name=nav_text)

            nav_item.click()
            time.sleep(0.5)

            # For overflow menu, we need to click each item in the dropdown
            if nav_text == 'more_horiz':
                # Get items from the dropdown menu
                menu_items = page.locator('[role="menu"] [role="menuitem"]').all()
                for menu_item in menu_items:
                    try:
                        item_text = menu_item.inner_text(timeout=1000).strip()
                        if item_text:
                            print(f'  Processing overflow item: {item_text}', file=sys.stderr)
                            menu_item.click()
                            time.sleep(0.5)
                            wait_for_content(page, timeout=5000)
                            expand_all_side_nav()
                            collect_leaf_urls()
                            # Re-open overflow menu for next item
                            nav_item = main_nav.get_by_role('link', name='Further menuitems')
                            nav_item.click()
                            time.sleep(0.3)
                    except Exception:
                        continue
            else:
                wait_for_content(page, timeout=5000)
                expand_all_side_nav()
                collect_leaf_urls()

            print(f'  Found {len(discovered)} URLs so far', file=sys.stderr)

        except Exception as e:
            print(f'Error processing {nav_text}: {e}', file=sys.stderr)
            continue

    return sorted(list(discovered))


def crawl_page(page: Page, hash_path: str) -> PageContent | None:
    """Navigate to a page and extract its content.

    Returns PageContent or None if failed.
    """
    try:
        # Check if we need a full page load or just hash navigation
        current_url = page.url
        if not current_url.startswith(BASE_URL):
            # Need full page load
            page.goto(BASE_URL + hash_path)
            if not wait_for_content(page):
                print(f'Timeout waiting for content: {hash_path}', file=sys.stderr)
                return None
        else:
            # Already on the site - use hash navigation (faster, SPA-friendly)
            page.evaluate(f'window.location.hash = "{hash_path}"')
            # Wait for content to update
            time.sleep(0.5)

        # Get main content HTML
        main = page.locator('[role="main"]').first

        # Wait for main to be visible (shorter timeout since page should be loaded)
        try:
            main.wait_for(state='visible', timeout=5000)
        except PlaywrightTimeout:
            print(f'Timeout waiting for main element: {hash_path}', file=sys.stderr)
            return None

        html = main.inner_html()

        # Get page title
        title = page.title()

        return PageContent(
            url=BASE_URL + hash_path,
            hash_path=hash_path,
            html=html,
            title=title
        )

    except Exception as e:
        print(f'Error crawling {hash_path}: {e}', file=sys.stderr)
        return None


def download_image(page: Page, url: str) -> bytes | None:
    """Download an image and return its bytes."""
    try:
        response = page.request.get(url)
        if response.ok:
            return response.body()
        return None
    except Exception as e:
        print(f'Error downloading image {url}: {e}', file=sys.stderr)
        return None


def extract_links(page: Page) -> list[str]:
    """Extract navigation links from the current page using JavaScript.

    Returns list of hash paths (e.g., ['#/get-started/quick-start', ...])
    discovered from the current page's navigation.
    """
    # Use JavaScript to extract all hash links efficiently without clicking
    links = page.evaluate('''() => {
        const links = new Set();

        // Get all anchor tags with hash hrefs
        document.querySelectorAll('a[href^="#/"]').forEach(a => {
            let href = a.getAttribute('href');
            if (href && href !== '#/') {
                // Remove any section anchor (e.g., "#/page/path#section" -> "#/page/path")
                // These are same-page anchors, not separate pages
                const sectionIdx = href.indexOf('#', 2);  // Find # after the initial #/
                if (sectionIdx > 0) {
                    href = href.substring(0, sectionIdx);
                }
                if (href !== '#/') {
                    links.add(href);
                }
            }
        });

        // Also check onclick handlers that set location.hash
        // by looking at navigation-related elements
        document.querySelectorAll('[data-role*="nav"], [role="navigation"], nav').forEach(nav => {
            nav.querySelectorAll('a, button').forEach(el => {
                let href = el.getAttribute('href');
                if (href && href.startsWith('#/') && href !== '#/') {
                    // Remove section anchors
                    const sectionIdx = href.indexOf('#', 2);
                    if (sectionIdx > 0) {
                        href = href.substring(0, sectionIdx);
                    }
                    if (href !== '#/') {
                        links.add(href);
                    }
                }
            });
        });

        return Array.from(links);
    }''')

    # Also expand one level of side nav and click through to discover children
    # but limit to just a few items to keep it fast
    discovered = set(links)

    # Click through visible leaf nav buttons (those without 'add' icon)
    # but limit to first 10 to keep it fast
    try:
        buttons = page.locator('nav button, [role="navigation"] button').all()
        clicked = 0
        max_clicks = 10

        for btn in buttons:
            if clicked >= max_clicks:
                break
            try:
                if not btn.is_visible():
                    continue

                btn_text = btn.inner_text(timeout=200)

                # Skip expand/collapse buttons
                if 'add' in btn_text or 'remove' in btn_text:
                    continue

                btn.click()
                time.sleep(0.1)
                clicked += 1

                current_hash = page.evaluate('() => window.location.hash')
                if current_hash and current_hash != '#/':
                    # Strip section anchors
                    current_hash = normalize_hash_path(current_hash)
                    if current_hash:
                        discovered.add(current_hash)

            except Exception:
                continue
    except Exception:
        pass

    return list(discovered)


def normalize_hash_path(hash_path: str) -> str | None:
    """Normalize a hash path by removing section anchors.

    '#/widgets/button#section' -> '#/widgets/button'
    '#/' -> None (home page, skip)
    """
    if not hash_path or hash_path == '#/':
        return None

    # Find section anchor (second # after initial #/)
    section_idx = hash_path.find('#', 2)
    if section_idx > 0:
        hash_path = hash_path[:section_idx]

    return hash_path if hash_path != '#/' else None
