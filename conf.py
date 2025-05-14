# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath("evpv"))  # Adjust if your submodule is deeper

project = 'EVPV'
copyright = '2024, Jeremy Dumoulin'
author = 'Jeremy Dumoulin'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc', 'sphinx.ext.mathjax']

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
        'processEscapes': True,
    },
    'options': {
        'skipStartupTypeset': True,
    }
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_logo = "img/logo_small.png"

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_show_sourcelink = False

html_context = {
    "display_github": True,
}
html_theme_options = {
    "github_url": "https://github.com/evpv-simulator"  # Direct link to the org page
}


