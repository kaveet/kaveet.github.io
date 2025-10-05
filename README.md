# kaveet.github.io

Field Notes - A documentation site built with Sphinx and the ReadTheDocs theme.

## About

This repository contains technical documentation built with [Sphinx](https://www.sphinx-doc.org/) and styled with the [ReadTheDocs theme](https://sphinx-rtd-theme.readthedocs.io/).

## Local Development

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kaveet/kaveet.github.io.git
   cd kaveet.github.io
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Building the Documentation

To build the HTML documentation locally:

```bash
cd docs
make html
```

The generated documentation will be in `docs/_build/html/`. You can open `docs/_build/html/index.html` in your browser to view it.

### Live Preview

To rebuild the documentation automatically when files change, you can use `sphinx-autobuild`:

```bash
pip install sphinx-autobuild
cd docs
sphinx-autobuild . _build/html
```

Then open http://127.0.0.1:8000 in your browser.

**Note**: Make sure your virtual environment is activated when running these commands.

### Cleaning Build Files

To clean all build artifacts:

```bash
cd docs
make clean
```

## Deployment

The documentation is automatically built and deployed to GitHub Pages when changes are pushed to the `main` branch. The GitHub Actions workflow handles:

1. Installing dependencies
2. Building the Sphinx documentation
3. Deploying to GitHub Pages

The site will be available at: https://kaveet.github.io

### GitHub Pages Configuration

To enable GitHub Pages deployment:

1. Go to your repository settings
2. Navigate to Pages (under Code and automation)
3. Under "Build and deployment", set:
   - **Source**: GitHub Actions

## Project Structure

```
kaveet.github.io/
├── .github/
│   └── workflows/
│       └── docs.yml          # GitHub Actions workflow
├── docs/
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Main documentation file
│   ├── Makefile             # Build commands for Unix
│   └── make.bat             # Build commands for Windows
├── .gitignore
├── requirements.txt         # Python dependencies
├── LICENSE
└── README.md
```

## Writing Documentation

Documentation is written in reStructuredText (`.rst`) format. Add new pages in the `docs/` directory and reference them in `docs/index.rst` using the `toctree` directive.

For more information on reStructuredText syntax, see the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

## License

MIT License - see LICENSE file for details.

