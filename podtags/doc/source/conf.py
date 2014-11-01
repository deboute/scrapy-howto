# -*- coding: utf-8 -*-
#
# scrapy-howto-podtags documentation build configuration file, created by
# sphinx-quickstart on Thu Oct 30 17:41:35 2014.
#
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]
autoclass_content = 'both'
autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'scrapy-howto-podtags'
copyright = u'2014, Benjamin Debouté'
version = '0.1.0'
release = '0.1.0'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'nature'
html_short_title = "Scrapy Howto: podtags"
html_static_path = ['_static']
htmlhelp_basename = 'scrapy-howto-podtagsdoc'
