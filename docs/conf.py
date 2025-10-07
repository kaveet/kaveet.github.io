# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Field Notes'
copyright = '2025, Kaveet Laxmidas'
author = 'Kaveet Laxmidas'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_prompt',
]

# MyST Parser configuration
myst_enable_extensions = [
    'substitution',
    'colon_fence',
]

myst_substitutions = {
    'mt8766_warning': '''```{warning}
This guide is for **MT6761 (Helio A22)** devices only. If you have an **MT8766** processor, see the [MT8766 disclaimer](mt8766-disclaimer) before proceeding.
```''',
    'mt8766_warning_subdir': '''```{warning}
This guide is for **MT6761 (Helio A22)** devices only. If you have an **MT8766** processor, see the [MT8766 disclaimer](../mt8766-disclaimer) before proceeding.
```''',
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# sphinx-copybutton configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# Configure "Edit this page" links
html_context = {
    'display_github': True,
    'github_user': 'kaveet',
    'github_repo': 'kaveet.github.io',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}
