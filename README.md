# A12 Widget Docs

The documentation of the A12 widgets, taken from the [A12 Widget Showcase](https://www.mgm-tp.com/a12.htmlshowcase/#/) in an LLM-friendly format - Markdown with locally downloaded images.

## Prerequisites

- Python 3.8+
- Playwright browser (Chromium)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd a12_widget_docs
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Usage

Run the scraper from the project root:

```bash
python -m src.main
```

The tool will:
1. Launch a headless browser and navigate to the A12 Widget Showcase
2. Detect the current documentation version
3. Discover all pages by traversing the navigation
4. Extract content from each page and convert to Markdown
5. Download all referenced images

## Output

The tool creates a directory named `A12_Widget_Documentation_<version>` (e.g., `A12_Widget_Documentation_38.1.1`) containing:

```
A12_Widget_Documentation_38.1.1/
├── GetStarted.QuickStart/
│   ├── index.md
│   └── image001.png
├── Basics.Forms/
│   ├── index.md
│   └── ...
├── Widgets.General.Buttons.Button/
│   ├── index.md
│   ├── example001.png
│   └── example002.png
└── ...
```

- Each documentation page becomes a directory with PascalCase dot-notation naming
- Page content is saved as `index.md`
- Images are downloaded and saved alongside the Markdown files
- Internal links are transformed to relative Markdown links

## How It Works

1. **URL Discovery**: Uses Playwright to expand all navigation items and collect all page URLs from the SPA
2. **Content Extraction**: Navigates to each page, waits for rendering, and extracts the main content
3. **Markdown Conversion**: Converts HTML to Markdown while preserving code blocks and formatting
4. **Asset Handling**: Downloads images and updates references to local paths
