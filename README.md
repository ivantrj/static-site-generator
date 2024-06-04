Absolutely, here's the converted text in markdown format:

## Static Site Generator

### Overview

This project is a static site generator that converts Markdown files into HTML pages using a predefined template. It processes Markdown content, applies a template, and outputs the resulting HTML files to a specified directory.

#### Project Structure

```
src/
    Contains the main source code.
    main.py: Main script to generate HTML pages.
    copystatic.py: Utility to copy static files.
    markdown_blocks.py: Converts Markdown to HTML nodes.
    inline_markdown.py: Handles inline Markdown elements.
    htmlnode.py: Defines HTML node structures.
    textnode.py: Defines text node structures.
content/
    Directory containing Markdown files to be processed.
static/
    Directory containing static assets (e.g., CSS).
public/
    Output directory for generated HTML files.
template.html: HTML template for the generated pages.
tests/
    Contains unit tests for the project.
```

### How to Run

1. **Install Dependencies:** Ensure you have Python installed.
2. **Generate HTML Pages:**

```bash
python main.py
```

3. **Serve the Site:**

```bash
cd public
python -m http.server 8888
```

This will start a local server at http://localhost:8888.

### Example Usage

1. **Generate Pages:**

```bash
python main.py
```

This will process Markdown files in the `content/` directory and output HTML files to the `public/` directory.

2. **Serve the Site:**

```bash
cd public
python -m http.server 8888
```

Access the site at http://localhost:8888.

### Testing

Run the unit tests using:

```bash
python -m unittest discover -s src
```




