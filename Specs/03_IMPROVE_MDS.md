# Improve Scraped Markdown Quality

## Goal

Clean the scraped A12 widget documentation markdown files so they are optimized for AI consumption. The docs will be used to give an LLM knowledge about A12 widgets.

## Issues to Fix

| Issue | Example | Action |
|-------|---------|--------|
| Icon placeholders | `*link*`, `*bug_report*` | Remove entirely |
| Concatenated demo labels | `*search*Default*visibility*Active` | Remove (keep code examples) |
| Breadcrumb navigation | `- Widgets\n  /\n- General` | Remove |
| Line numbers in code | `1import {\n2 A11Y...` | Strip line numbers |
| Copy button artifacts | `*content_copy*` | Remove |
| Malformed internal links | `(../Widget#section/index.md)` | Fix to `(../Widget/index.md#section)` |

## Approach

**Post-processing script** (`src/clean_markdown.py`)

Run a Python script that reads from the original scraped files and writes cleaned versions to a separate output directory. Original files remain untouched.

```
Input:  A12_Widget_Documentation_38.1.1/        (original, read-only)
Output: A12_Widget_Documentation_38.1.1_clean/  (cleaned output)
```

## Cleaning Rules

### 1. Remove breadcrumb block at document start

The pattern appears at the top of each file:
```
- Widgets
  /
- General
  /
- Buttons
```

### 2. Remove icon placeholders

Strip Material icon names that appear as `*icon_name*` (e.g., `*search*`, `*content_copy*`, `*center_focus_weak*`).

Use a whitelist of known Material icon names to avoid removing legitimate italic text.

### 3. Clean code blocks

- Strip leading line numbers (`1`, `2`, etc.) from code lines
- Remove `*content_copy*` that appears after code blocks

### 4. Fix internal links

Transform `(../Widgets.General.Buttons.Button#invertButtons/index.md)` to `(../Widgets.General.Buttons.Button/index.md#invertButtons)`

### 5. Remove visual demo artifacts

Lines like `PrimarySecondary` or `Loading LoadingSecondaryLoading Loading` are rendered button states with no value for AI comprehension. Remove these orphan label concatenations.

## Table of Contents

Generate `A12_Widget_Documentation_38.1.1/INDEX.md` with a hierarchical listing of all 47 widget docs. This helps an AI quickly understand the scope and navigate to relevant sections.

Structure:
```markdown
# A12 Widget Documentation Index

## Getting Started
- [Home](./Home/index.md)
- [Get Started](./GetStarted/index.md)
  - [Use and Configure Widgets Style](./GetStarted.UseAndConfigureWidgetsStyle/index.md)

## Basics
- [Basics](./Basics/index.md)
- [Accessibility](./Basics.Accessibility/index.md)
- Theme
  - [Colors](./Basics.Theme.Colors/index.md)
  ...

## Widgets
- General
  - [Button](./Widgets.General.Buttons.Button/index.md)
  - [Icon](./Widgets.General.Icon/index.md)
  - [Link](./Widgets.General.Link/index.md)
- Data Display
  - [Table](./Widgets.DataDisplay.Table/index.md)
  ...
```

## Output

- Format: GitHub-flavored markdown
- Cleaned files written to `_clean/` directory
- Original scraped files remain untouched
- INDEX.md generated in the clean output directory
