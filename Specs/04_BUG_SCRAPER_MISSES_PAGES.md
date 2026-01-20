# Bug: Scraper Misses Pages

## Problem
The scraper discovered only 45 pages, but the live site has 80+. Missing entire categories (Utils, Business Case, FAQ) and many sub-pages within scraped categories.

## Root Cause
The current `discover_urls()` in `crawler.py` uses brittle heuristics—matching button text like `'add'`/`'remove'` to detect expandable nav items. This fails when the nav structure uses different patterns or has deeply nested items.

## Solution: Use the Search Dialog Index
The site's search feature (Cmd+K) opens a dialog containing a **complete categorized index of all pages**. Each page is a button that navigates to the corresponding hash URL.

**Why this works:**
- The search index is the source of truth for navigation
- Single dialog contains all pages—no multi-level traversal needed
- More stable than sidebar heuristics

**Approach:**
1. Open search dialog (click search box)
2. Extract all page entries from the dialog
3. Click each entry to capture its hash URL

```python
def discover_urls_via_search(page: Page) -> list[str]:
    page.click('[placeholder="Search..."]')
    page.wait_for_selector('dialog')

    discovered = set()
    buttons = page.locator('dialog button').all()
    for btn in buttons:
        btn.click()
        hash_url = page.evaluate('window.location.hash')
        if hash_url and hash_url != '#/':
            discovered.add(hash_url)
        page.click('[placeholder="Search..."]')

    return sorted(discovered)
```

## Next Steps
- [x] Implement comprehensive URL discovery in `crawler.py`
- [x] Validate discovered URLs against known missing pages

## Implementation Notes

The original spec proposed using the search dialog, but testing revealed it only contains ~40 pages (not the full index). Instead, the solution uses a sidebar traversal approach that handles the accordion behavior (only one category expanded at a time).

The `discover_urls_via_search()` function now:
1. Visits each main navigation section (Get Started, Basics, Widgets, etc.)
2. Processes each category by expanding it and clicking all leaf items
3. Handles nested categories (e.g., Widgets > General > Buttons > Button)
4. Discovers 92 URLs total (exceeding the 80+ target)
