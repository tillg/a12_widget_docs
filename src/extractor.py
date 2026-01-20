"""HTML to Markdown conversion and image handling."""

import re
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse

from markdownify import markdownify as md, MarkdownConverter


@dataclass
class ExtractedContent:
    """Result of content extraction."""
    markdown: str
    image_urls: list[str]


class CustomConverter(MarkdownConverter):
    """Custom markdown converter with better code block handling."""

    def convert_pre(self, el, text, parent_tags=None):
        """Convert pre elements to fenced code blocks."""
        # Try to detect language from class
        code_el = el.find('code')
        lang = ''

        if code_el:
            classes = code_el.get('class', [])
            if isinstance(classes, str):
                classes = classes.split()
            for cls in classes:
                if cls.startswith('language-'):
                    lang = cls.replace('language-', '')
                    break
                elif cls in ('typescript', 'javascript', 'html', 'css', 'json', 'xml', 'bash', 'shell'):
                    lang = cls
                    break

        # Get the text content
        code_text = el.get_text()

        return f'\n```{lang}\n{code_text}\n```\n'

    def convert_code(self, el, text, parent_tags=None):
        """Convert inline code elements."""
        # Check if this is inside a pre - if so, just return text
        if el.parent and el.parent.name == 'pre':
            return text
        return f'`{text}`'


def extract_content(html: str, base_url: str, current_hash: str) -> ExtractedContent:
    """Extract markdown content and image URLs from HTML.

    Args:
        html: The HTML content of the main element
        base_url: The base URL for resolving relative URLs
        current_hash: The current hash path for link transformation

    Returns:
        ExtractedContent with markdown and list of image URLs
    """
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')

    # Collect image URLs before conversion
    image_urls = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            # Resolve relative URLs
            full_url = urljoin(base_url, src)
            image_urls.append(full_url)

    # Convert to markdown using custom converter
    markdown = CustomConverter(
        heading_style='atx',
        bullets='-',
        code_language='',
        strip=['script', 'style', 'nav'],
    ).convert(str(soup))

    # Clean up excessive whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    markdown = markdown.strip()

    return ExtractedContent(markdown=markdown, image_urls=image_urls)


def transform_links(markdown: str, current_dir: str, base_url: str) -> str:
    """Transform internal links to relative markdown links.

    Converts links like:
        [Text](#/path/to/page) -> [Text](../Path.To.Page/index.md)
    """
    from .storage import hash_path_to_directory

    def replace_link(match):
        text = match.group(1)
        href = match.group(2)

        # Check if it's an internal hash link
        if href.startswith('#/'):
            target_dir = hash_path_to_directory(href)
            return f'[{text}](../{target_dir}/index.md)'

        # Check if it's same-site link
        parsed = urlparse(href)
        if parsed.fragment and parsed.fragment.startswith('/'):
            target_dir = hash_path_to_directory('#' + parsed.fragment)
            return f'[{text}](../{target_dir}/index.md)'

        return match.group(0)

    # Match markdown links: [text](url)
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.sub(pattern, replace_link, markdown)


def update_image_references(markdown: str, url_to_filename: dict[str, str]) -> str:
    """Update image references in markdown to use local filenames."""
    result = markdown
    for url, filename in url_to_filename.items():
        # Escape special regex characters in URL
        escaped_url = re.escape(url)
        # Replace full URL references
        result = re.sub(escaped_url, filename, result)

        # Also replace relative path references (e.g., "images/foo.png" from the original HTML)
        parsed = urlparse(url)
        if parsed.path:
            # Get the relative path portion (remove leading slash if present)
            rel_path = parsed.path.lstrip('/')
            # Remove the base path if it's part of the URL (e.g., "a12.htmlshowcase/")
            if '/' in rel_path:
                # Try progressively shorter paths to find matches
                parts = rel_path.split('/')
                for i in range(len(parts)):
                    partial_path = '/'.join(parts[i:])
                    if partial_path and partial_path != filename:
                        escaped_partial = re.escape(partial_path)
                        result = re.sub(escaped_partial, filename, result)
    return result
