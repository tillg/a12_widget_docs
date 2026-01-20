"""Post-process scraped markdown files for AI consumption.

Reads from original scraped directory, applies cleaning rules,
writes to a separate clean output directory.
"""

import re
import shutil
from pathlib import Path

# Common Material Design icon names found in the scraped docs
MATERIAL_ICONS = {
    'link', 'code', 'bug_report', 'center_focus_weak', 'search', 'visibility',
    'delete', 'get_app', 'fullscreen_exit', 'content_copy', 'open_in_new',
    'api', 'palette', 'info', 'warning', 'error', 'check', 'close', 'add',
    'remove', 'edit', 'save', 'refresh', 'settings', 'menu', 'home',
    'arrow_back', 'arrow_forward', 'arrow_drop_down', 'arrow_drop_up',
    'expand_more', 'expand_less', 'more_vert', 'more_horiz', 'star',
    'favorite', 'share', 'download', 'upload', 'print', 'filter_list',
    'sort', 'keyboard_arrow_left', 'keyboard_arrow_right', 'first_page',
    'last_page', 'chevron_left', 'chevron_right', 'play_arrow', 'pause',
    'stop', 'skip_next', 'skip_previous', 'volume_up', 'volume_down',
    'volume_mute', 'fullscreen', 'zoom_in', 'zoom_out', 'lock', 'lock_open',
    'person', 'people', 'group', 'notifications', 'email', 'phone', 'place',
    'calendar_today', 'schedule', 'access_time', 'date_range', 'event',
    'attach_file', 'cloud', 'cloud_upload', 'cloud_download', 'folder',
    'folder_open', 'insert_drive_file', 'description', 'image', 'photo',
    'camera', 'videocam', 'mic', 'headset', 'computer', 'smartphone',
    'tablet', 'tv', 'watch', 'keyboard', 'mouse', 'memory', 'storage',
    'dns', 'http', 'vpn_key', 'security', 'verified_user', 'help',
    'help_outline', 'info_outline', 'warning_amber', 'error_outline',
    'cancel', 'check_circle', 'highlight_off', 'add_circle', 'remove_circle',
}


def remove_breadcrumbs(content: str) -> str:
    """Remove breadcrumb navigation block from start of document.

    Pattern:
    - Widgets\n\n  /\n- General\n\n  /\n- Buttons\n\n  /\n- Button\n\n
    """
    # Match breadcrumb pattern: repeated (- text\n\n  /\n) ending with (- text\n\n)
    # All items including the last one may have the trailing "  /\n"
    pattern = r'^(# .+\n\n)((?:- .+\n\n  /\n)*- .+\n\n)'
    match = re.match(pattern, content)
    if match:
        return match.group(1) + content[match.end():]

    return content


def remove_icon_placeholders(content: str) -> str:
    """Remove Material icon placeholders like *link*, *code*, *bug_report*.

    Also handles compound icons like *infoInformation*, *warningWarning*.
    Handles escaped underscores: *get\\_app*
    """

    def is_icon(text: str) -> bool:
        """Check if text matches a known Material icon."""
        # Normalize: remove backslash escapes and lowercase
        normalized = text.replace('\\', '').lower()

        # Direct match
        if normalized in MATERIAL_ICONS:
            return True

        # Check if starts with a known icon (for compound names)
        for icon in MATERIAL_ICONS:
            if normalized.startswith(icon):
                return True

        # Check underscore-separated (e.g., get_app, center_focus_weak)
        if '_' in normalized:
            base = normalized.split('_')[0]
            if base in MATERIAL_ICONS:
                return True

        return False

    def replace_icon(match):
        icon_text = match.group(1)
        if is_icon(icon_text):
            return ''
        return match.group(0)

    # Match *word* patterns (may contain underscores, backslashes for escaping)
    # Pattern: *text_with_possible\_escapes*
    content = re.sub(r'\*([a-zA-Z][a-zA-Z_\\]*)\*', replace_icon, content)

    # Remove consecutive icons like *code**center_focus_weak**bug_report*
    content = re.sub(r'(\*[a-zA-Z][a-zA-Z_\\]*\*){2,}', '', content)

    return content


def clean_code_blocks(content: str) -> str:
    """Remove line numbers from code blocks and content_copy artifacts."""

    def clean_code_block(match):
        lang = match.group(1) or ''
        code = match.group(2)

        lines = code.split('\n')
        cleaned_lines = []
        for line in lines:
            # Skip lines that are just a number (orphan line numbers)
            if re.match(r'^\d+$', line.strip()):
                continue

            # Remove line numbers at start of lines (e.g., "1import", "2  const")
            cleaned = re.sub(r'^(\d+)(?=[a-zA-Z"\'{}\[\]<>/\s])', '', line)

            # Remove content_copy at end of line (with or without asterisks)
            cleaned = re.sub(r'\*?content_?copy\*?$', '', cleaned)
            cleaned = re.sub(r'\*?content\\_copy\*?$', '', cleaned)

            cleaned_lines.append(cleaned)

        cleaned_code = '\n'.join(cleaned_lines)
        return f'```{lang}\n{cleaned_code}```'

    # Match code blocks
    content = re.sub(r'```(\w*)\n(.*?)```', clean_code_block, content, flags=re.DOTALL)

    # Remove *content_copy* after code blocks (standalone line)
    content = re.sub(r'```\n\*?content_?copy\*?\n', '```\n', content)
    content = re.sub(r'```\n\*?content\\_copy\*?\n', '```\n', content)

    return content


def fix_internal_links(content: str) -> str:
    """Fix malformed internal links.

    Transform: (../Widgets.General.Buttons.Button#invertButtons/index.md)
    To: (../Widgets.General.Buttons.Button/index.md#invertButtons)
    """
    # Pattern: (../Path#anchor/index.md) -> (../Path/index.md#anchor)
    def fix_link(match):
        path = match.group(1)
        anchor = match.group(2)
        return f'(../{path}/index.md#{anchor})'

    content = re.sub(r'\(\.\./([^#)]+)#([^/]+)/index\.md\)', fix_link, content)

    return content


def remove_demo_artifacts(content: str) -> str:
    """Remove visual demo artifacts like concatenated button labels.

    Patterns like:
    - PrimarySecondary
    - Loading LoadingSecondaryLoading Loading
    - DefaultActiveDestructiveDisabled
    """
    # Known button state words that appear in demos
    button_states = {'Primary', 'Secondary', 'Default', 'Active', 'Destructive',
                     'Disabled', 'Loading', 'Inverted', 'Regular', 'Activated'}

    lines = content.split('\n')
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()

        # Skip empty lines - keep them
        if not stripped:
            cleaned_lines.append(line)
            continue

        # Remove any remaining icon placeholders from the line for analysis
        test_line = re.sub(r'\*[a-zA-Z_\\]+\*', '', stripped).strip()

        # Check if line is purely button states concatenated
        # Split on spaces and check each "word"
        words = test_line.split()
        if words:
            all_button_states = True
            for word in words:
                # Check if word is concatenated button states
                # e.g., "PrimarySecondary" or "LoadingSecondaryLoading"
                remaining = word
                found_any = False
                while remaining:
                    matched = False
                    for state in button_states:
                        if remaining.startswith(state):
                            remaining = remaining[len(state):]
                            matched = True
                            found_any = True
                            break
                    if not matched:
                        break
                if remaining or not found_any:
                    all_button_states = False
                    break

            if all_button_states and len(test_line) > 0:
                continue

        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)


def clean_empty_lines(content: str) -> str:
    """Normalize multiple consecutive empty lines to maximum of 2."""
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    return content


def clean_markdown(content: str) -> str:
    """Apply all cleaning rules to markdown content."""
    content = remove_breadcrumbs(content)
    content = remove_icon_placeholders(content)
    content = clean_code_blocks(content)
    content = fix_internal_links(content)
    content = remove_demo_artifacts(content)
    content = clean_empty_lines(content)
    return content.strip() + '\n'


def generate_index(docs_dir: Path) -> str:
    """Generate INDEX.md with hierarchical listing of all docs."""

    folders = sorted([f.name for f in docs_dir.iterdir() if f.is_dir()])

    # Organize by category
    categories = {
        'Getting Started': [],
        'Basics': [],
        'Examples': [],
        'Experimental': [],
        'Widgets': {},
    }

    for folder in folders:
        if folder == 'Home':
            categories['Getting Started'].insert(0, ('Home', folder))
        elif folder.startswith('GetStarted'):
            name = folder.replace('GetStarted.', '').replace('GetStarted', 'Get Started')
            name = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)  # CamelCase to spaces
            categories['Getting Started'].append((name, folder))
        elif folder.startswith('Basics'):
            name = folder.replace('Basics.', '').replace('Basics', 'Overview')
            name = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
            categories['Basics'].append((name, folder))
        elif folder.startswith('Examples'):
            name = folder.replace('Examples.', '').replace('Examples', 'Overview')
            name = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
            categories['Examples'].append((name, folder))
        elif folder.startswith('Experimental'):
            name = folder.replace('Experimental.', '').replace('Experimental', 'Overview')
            name = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
            categories['Experimental'].append((name, folder))
        elif folder.startswith('Widgets'):
            # Parse widget category: Widgets.Category.SubCategory.Name
            parts = folder.split('.')
            if len(parts) >= 3:
                widget_category = parts[1]  # e.g., "General", "DataDisplay"
                widget_category = re.sub(r'([a-z])([A-Z])', r'\1 \2', widget_category)
                widget_name = '.'.join(parts[2:])
                widget_name = re.sub(r'([a-z])([A-Z])', r'\1 \2', widget_name)

                if widget_category not in categories['Widgets']:
                    categories['Widgets'][widget_category] = []
                categories['Widgets'][widget_category].append((widget_name, folder))
            else:
                # Just "Widgets" overview
                categories['Widgets']['_overview'] = ('Widgets Overview', folder)

    # Build markdown
    lines = ['# A12 Widget Documentation Index\n']

    # Getting Started
    if categories['Getting Started']:
        lines.append('## Getting Started\n')
        for name, folder in categories['Getting Started']:
            lines.append(f'- [{name}](./{folder}/index.md)')
        lines.append('')

    # Basics
    if categories['Basics']:
        lines.append('## Basics\n')
        for name, folder in categories['Basics']:
            lines.append(f'- [{name}](./{folder}/index.md)')
        lines.append('')

    # Widgets
    if categories['Widgets']:
        lines.append('## Widgets\n')

        # Overview first
        if '_overview' in categories['Widgets']:
            name, folder = categories['Widgets']['_overview']
            lines.append(f'- [{name}](./{folder}/index.md)\n')

        # Then by category
        for cat in sorted(categories['Widgets'].keys()):
            if cat == '_overview':
                continue
            lines.append(f'### {cat}\n')
            for name, folder in sorted(categories['Widgets'][cat]):
                lines.append(f'- [{name}](./{folder}/index.md)')
            lines.append('')

    # Examples
    if categories['Examples']:
        lines.append('## Examples\n')
        for name, folder in categories['Examples']:
            lines.append(f'- [{name}](./{folder}/index.md)')
        lines.append('')

    # Experimental
    if categories['Experimental']:
        lines.append('## Experimental\n')
        for name, folder in categories['Experimental']:
            lines.append(f'- [{name}](./{folder}/index.md)')
        lines.append('')

    return '\n'.join(lines)


def process_directory(input_dir: Path, output_dir: Path) -> None:
    """Process all markdown files from input_dir to output_dir."""

    # Clean output directory if it exists
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    # Process each subdirectory
    processed = 0
    for subdir in sorted(input_dir.iterdir()):
        if not subdir.is_dir():
            continue

        index_file = subdir / 'index.md'
        if not index_file.exists():
            continue

        # Read, clean, write
        content = index_file.read_text(encoding='utf-8')
        cleaned = clean_markdown(content)

        # Create output subdirectory
        out_subdir = output_dir / subdir.name
        out_subdir.mkdir(parents=True, exist_ok=True)

        # Write cleaned file
        out_file = out_subdir / 'index.md'
        out_file.write_text(cleaned, encoding='utf-8')

        # Copy any other files (images, etc.)
        for other_file in subdir.iterdir():
            if other_file.name != 'index.md':
                shutil.copy2(other_file, out_subdir / other_file.name)

        processed += 1

    # Generate INDEX.md
    index_content = generate_index(output_dir)
    (output_dir / 'INDEX.md').write_text(index_content, encoding='utf-8')

    print(f'Processed {processed} documents')
    print(f'Generated INDEX.md')
    print(f'Output: {output_dir}')


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Clean scraped markdown files')
    parser.add_argument('input_dir', nargs='?',
                        default='A12_Widget_Documentation_38.1.1',
                        help='Input directory with scraped docs')
    parser.add_argument('output_dir', nargs='?',
                        default=None,
                        help='Output directory (default: input_dir + "_clean")')

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir) if args.output_dir else Path(str(input_dir) + '_clean')

    if not input_dir.exists():
        print(f'Error: Input directory not found: {input_dir}')
        return 1

    process_directory(input_dir, output_dir)
    return 0


if __name__ == '__main__':
    exit(main())
