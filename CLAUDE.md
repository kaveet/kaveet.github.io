# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Sphinx-based documentation site ("Field Notes") deployed to GitHub Pages. The site uses MyST-Parser for Markdown support and the ReadTheDocs theme for styling.

## Development Commands

### Environment Setup
```bash
make install  # Creates venv and installs all dependencies
source venv/bin/activate  # Activate virtual environment
```

### Common Development Tasks
```bash
make dev     # Start live preview server at http://127.0.0.1:8000 with auto-reload
make build   # Build the documentation (outputs to docs/_build/html/)
make clean   # Remove all build artifacts
```

### Manual Sphinx Commands (when in docs/ directory)
```bash
cd docs
make html    # Build HTML documentation
make clean   # Clean build files
sphinx-autobuild . _build/html --open-browser  # Live preview
```

## Architecture

### Project Structure
- `/docs/` - All documentation content and Sphinx configuration
  - `conf.py` - Sphinx configuration file
  - `index.md` - Root documentation page
  - Content organized in subdirectories (e.g., `dumbphones/`)
- `/docs/_build/` - Generated HTML output (gitignored)
- Root `Makefile` - Development task automation
- `requirements.txt` - Python dependencies

### Documentation System
- **Format**: MyST-Markdown (`.md` files) with MyST-Parser
- **Theme**: sphinx_rtd_theme (ReadTheDocs)
- **Extensions**: myst_parser, sphinx_design, sphinx_copybutton, sphinx_prompt
- **MyST Features Enabled**: substitution, colon_fence

### Content Organization
- Documentation is hierarchical using `toctree` directives
- Each section should have an `index.md` that includes a toctree
- MyST substitutions are defined in `docs/conf.py` under `myst_substitutions`

### Deployment
- Automatic deployment to GitHub Pages via `.github/workflows/docs.yml`
- Triggers on push to `main` branch
- Important: `.nojekyll` file must be present in build output to prevent Jekyll processing

## Working with Documentation

### Adding New Pages
1. Create `.md` file in appropriate `docs/` subdirectory
2. Add reference to parent section's `index.md` toctree directive
3. Use MyST-Markdown syntax (see https://myst-parser.readthedocs.io/)

### Using MyST Substitutions
Predefined substitutions are available in conf.py (e.g., `{{mt8766_warning}}`). Add new substitutions to `myst_substitutions` dictionary.

### Using sphinx-prompt
Use the `prompt` directive for shell commands with proper prompt indicators:
````markdown
```{prompt} bash $
make install
make dev
```
````

### GitHub Integration
"Edit this page" links are configured in `html_context` in conf.py pointing to the main branch.
- the project uses Markdown instead of ReStructuredText