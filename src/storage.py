"""File and image saving, path conversion utilities."""

import re
from pathlib import Path
from urllib.parse import urlparse


def kebab_to_pascal(segment: str) -> str:
    """Convert kebab-case to PascalCase.

    Example: 'quick-start' -> 'QuickStart'
    """
    return ''.join(word.capitalize() for word in segment.split('-'))


def hash_path_to_directory(hash_path: str) -> str:
    """Convert URL hash path to directory name.

    Rules:
    1. Split path on '/'
    2. Convert each segment from kebab-case to PascalCase
    3. Join segments with '.'

    Example: '#/get-started/quick-start' -> 'GetStarted.QuickStart'
    """
    # Remove leading '#/' or '/'
    path = hash_path.lstrip('#/')

    if not path:
        return 'Home'

    segments = [s for s in path.split('/') if s]
    pascal_segments = [kebab_to_pascal(seg) for seg in segments]
    return '.'.join(pascal_segments)


def save_markdown(output_dir: Path, dir_name: str, content: str) -> Path:
    """Save markdown content to the appropriate directory.

    Creates: output_dir/dir_name/index.md
    Returns the path to the saved file.
    """
    target_dir = output_dir / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)

    file_path = target_dir / 'index.md'
    file_path.write_text(content, encoding='utf-8')

    return file_path


def save_image(output_dir: Path, dir_name: str, image_data: bytes,
               original_url: str, index: int) -> str:
    """Save an image and return the local filename.

    Uses original filename if available, otherwise numbered (image001.png).
    """
    target_dir = output_dir / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)

    # Try to get original filename from URL
    parsed = urlparse(original_url)
    original_name = Path(parsed.path).name

    if original_name and '.' in original_name:
        # Sanitize filename
        filename = re.sub(r'[^\w.\-]', '_', original_name)
    else:
        # Use numbered fallback
        ext = '.png'  # Default extension
        if original_url.lower().endswith(('.jpg', '.jpeg')):
            ext = '.jpg'
        elif original_url.lower().endswith('.gif'):
            ext = '.gif'
        elif original_url.lower().endswith('.svg'):
            ext = '.svg'
        elif original_url.lower().endswith('.webp'):
            ext = '.webp'
        filename = f'image{index:03d}{ext}'

    file_path = target_dir / filename
    file_path.write_bytes(image_data)

    return filename


def transform_internal_link(from_dir: str, to_hash_path: str) -> str:
    """Transform an internal link to a relative markdown link.

    Example:
        from_dir='GetStarted.QuickStart'
        to_hash_path='#/basics/forms'
        -> '../Basics.Forms/index.md'
    """
    to_dir = hash_path_to_directory(to_hash_path)
    return f'../{to_dir}/index.md'
