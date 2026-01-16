# Retrieve Docs

Retrieve the A12 Widget documentation and save it locally as Markdown files.

## Requirements

- **Source**: `https://www.mgm-tp.com/a12.htmlshowcase/#/`
- **Output**: `A12_Widget_Documentation_<version>/` — version scraped from the site header (e.g., `38.1.1`)
- **Directory naming**: URL path → PascalCase with dots (e.g., `GetStarted.QuickStart/index.md`)
- **Images**: download referenced images alongside `index.md`, named by original filename or numbered (`image001.png`)
- **Code snippets**: triple-backtick fenced blocks
- **Content sections**: Each page has sections (Overview examples, API, Theming) as H2 headings on a single continuous page — capture all sections in one `index.md`
- **Internal links**: transform to relative Markdown links (`[Page Name](../Path.To.Page/index.md)`)
- **Python project**: modules in `src/`, `requirements.txt`, `.venv`

## Site Characteristics

- **SPA with hash routing**: URLs like `#/get-started/migration-instructions/migration-notes`
- **JavaScript-rendered**: Playwright required for content extraction
- **Deep hierarchy**: up to 4 levels (e.g., `#/widgets/general/buttons/button`)
- **Version location**: Displayed in header as a paragraph element (e.g., `38.1.1`)
- **Structure**: Top nav bar → Side navigation (expandable tree) → Main content area

## Navigation Structure

**Top navigation bar**: Links to main sections (Get Started, Basics, Widgets, etc.). Overflow items appear in a "Further menuitems" dropdown.

**Side navigation**: A tree of expandable/collapsible items:
- **Expandable items**: `<button>` elements with `aria-expanded` attribute
  - Collapsed: shows `add` icon (plus sign)
  - Expanded: shows `remove` icon (minus sign), children appear in a nested `<document>` element
- **Leaf items**: `<button>` elements without expand icons — clicking navigates to that page
- **Nested expandable**: Some items have children that are also expandable (indicated by `add` icon)

**Content area**: Single continuous page with multiple H2 sections (e.g., "Primary Buttons", "API", "Theming configuration"). No separate tabs — all content is on one scrollable page.

## Approach

1. **Discover URLs**: Recursively traverse the side navigation
   - Click each top nav item to load its section
   - Expand all collapsed nav items (click buttons with `add` icon)
   - Collect all leaf item URLs from the navigation tree

2. **Crawl sequentially**: Visit each URL via hash navigation
   - Wait for `[role="main"]` or `main` element to have content (length > 100 chars)
   - No rate limiting needed (same-origin SPA)

3. **Extract content**:
   - Target the `main` element for content extraction
   - Convert HTML to Markdown using `markdownify`
   - Preserve all H2 sections (examples, API, Theming)

4. **Save**: Write `index.md` + download images per directory

5. **Errors**: Log failures to stderr and continue with next page

## Wait Conditions

Content is considered fully rendered when:
- `document.readyState === 'complete'`
- `main` element exists and has substantial text content (> 100 characters)
- No loading/spinner elements present (check for `[class*="loading"]`, `[class*="spinner"]`)

## Module Structure

```
src/
  crawler.py      # Playwright navigation, URL discovery
  extractor.py    # HTML → Markdown conversion
  storage.py      # File/image saving
  main.py         # CLI entry point
```
