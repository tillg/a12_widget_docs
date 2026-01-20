# Persist Discovered URLs

Enable the scraper to resume from where it left off if interrupted.

## Requirements

- **Persist URLs**: Save discovered URLs to `pages.json` as they are found
- **Track progress**: Record scrape status with timestamps
- **Resume**: On restart, skip already-completed pages and retry failed ones
- **Progress bar**: Show completion status during scraping

## State File

**Location**: `A12_Widget_Documentation_<version>/pages.json`

```json
{
  "scrape": {
    "scrape_started": "2024-01-15T10:30:00Z",
    "scrape_finished": "2024-01-15T10:45:23Z"
  },
  "pages": [
    {
      "url": "#/get-started/quick-start",
      "scrape_started": "2024-01-15T10:30:05Z",
      "scrape_finished": "2024-01-15T10:30:12Z",
      "scrape_result": "success",
      "scrape_error": null
    }
  ]
}
```

**Page status values**: `null` (pending), `in_progress`, `success`, `error`

## Process Flow

Discovery and scraping are unified — new URLs are discovered while crawling pages.

### Scrape Loop

1. Pick next page where `scrape_result` is not `success`
2. Navigate to page, extract content
3. Extract links via JavaScript, add new URLs to queue (section anchors stripped)
4. Save markdown and images
5. Mark page as `success` or `error`
6. Save state
7. Repeat until no pending pages remain

### Resume Behavior

- **Interrupted scrape**: Reset `in_progress` and `error` pages to retry them
- **Completed scrape**: Start fresh re-scrape
- **Corrupted state file**: Log warning, start from scratch

## Progress Display

```
Scraping: [████████░░░░░░░░░░░░]  45/142 ( 32%) - #/basics/validation
```

```
Resuming: 45/142 pages already completed
Scraping: [████████░░░░░░░░░░░░]  45/142 ( 32%) - #/basics/validation
```

```
Done! Scraped 142 pages in 2m 34s
```

## Link Extraction

URLs are extracted using JavaScript DOM queries for `a[href^="#/"]` elements, with section anchors stripped (`#/page/path#section` → `#/page/path`) to avoid duplicate crawls.
