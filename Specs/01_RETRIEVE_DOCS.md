# Retrieve Docs

Retrieve the A12 Widget documentation and save it locally as Markdown files.

## Requirements

- **Source**: `https://www.mgm-tp.com/a12.htmlshowcase/#/`
- **Output**: `A12_Widget_Documentation_<version>/` — version scraped from the site header
- **Directory naming**: URL path converted to PascalCase with dots (see [Path Conversion](#path-conversion))
- **Images**: Downloaded alongside `index.md`, using original filename or numbered fallback
- **Code snippets**: Triple-backtick fenced blocks with language hints where detectable
- **Content sections**: All sections captured in one `index.md` per page
- **Internal links**: Transformed to relative Markdown links (`../Path.To.Page/index.md`)

## Path Conversion

| URL Hash Path | Directory |
|---------------|-----------|
| `#/` | `Home/index.md` |
| `#/get-started/quick-start` | `GetStarted.QuickStart/index.md` |
| `#/widgets/general/buttons/button` | `Widgets.General.Buttons.Button/index.md` |

## Site Characteristics

- **SPA with hash routing**: Playwright required for JavaScript-rendered content
- **Content element**: `[role="main"]` (not `<main>`)
- **Version location**: In header banner, extracted via regex `(\d+\.\d+\.\d+)`

## Project Structure

```
src/
  crawler.py      # Playwright navigation, link extraction
  extractor.py    # HTML → Markdown conversion, image handling
  storage.py      # File/image saving, path conversion
  main.py         # CLI entry point, state management
```

## Dependencies

```
playwright
markdownify
beautifulsoup4
```

## Usage

```bash
python -m src.main
```
