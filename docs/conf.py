# Configuration file for the Sphinx documentation builder.

import os, sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# -- Project information

project = 'MITIM'
copyright = '2018, Pablo RF'
author = 'Pablo Rodriguez-Fernandez'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output

on_rtd = os.environ.get('READTHEDOCS',None) == 'True'

on_rtd = False

if not on_rtd: # only import and set the theme if we're buiding docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {

# avoid empty pages:
'extraclassoptions': 'openany,oneside',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
'preamble': r'\hypersetup{bookmarksdepth=3}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'aurora.tex', u'Aurora Documentation',
   u'Francesco Sciortino', 'manual'),
]
