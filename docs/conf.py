# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'intel sphinx theme'
copyright = '2024, Intel'
author = 'Katarzyna Bojarowska'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinxcontrib.images',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx_design',
    'sphinx_togglebutton',
]

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for autoapi -------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../intel_sphinx_theme"]
autoapi_keep_files = True
autoapi_root = "api"
autoapi_member_order = "groupwise"

html_theme = "intel_sphinx_theme"

# Enabling building both themes
import os

# Make sure html_context is defined
html_context = globals().get("html_context", {})

# Use environment variable to override or default to existing context value
sub_theme = os.environ.get("SUBTHEME") or html_context.get("subtheme", "default")

# Set the color scheme in the context so templates have it
html_context["color_scheme"] = sub_theme
html_static_path = ['_static']

# Use the color scheme to decide theme variant or any config overrides
if sub_theme == "tb":
    html_context = {
        "color_scheme": "tb",
    }
else:
    html_context = {
        "color_scheme": "default",
    }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Set logo and favicon separately
html_logo = "_static/logo.svg"  # Logo shown in the navigation bar
html_favicon = "_static/favicon.svg"  # Favicon shown in the browser tab

html_theme_options = {
   "header_links_before_dropdown": 2,
   "show_prev_next": False,
    "check_switcher": False,
    "navbar_start": ["navbar-logo", "version-switcher"],
    #"navbar_end": ["navbar-icon-links", "version-switcher"],
     "primary_sidebar_end": ["version-switcher"]
}

html_context = {
   "default_mode": "auto",
   "header_variant": "spark-squares",
   #"header_variant": "spark-color",
   #"header_variant": "default",
   "footer_variant": "simple",
   "content_width": "large",
   'footer_links': [
        ('Terms of Use', 'https://www.intel.com/content/www/us/en/legal/terms-of-use.html'),
        ('Cookies', 'https://www.intel.com/content/www/us/en/privacy/intel-cookie-notice.html'),
        ('Privacy', 'https://www.intel.com/content/www/us/en/privacy/intel-privacy-notice.html'),
    ],
    'global_link_list': {
        'title': 'Created with',
        'links': [
            {'text': 'Sphinx', 'url': 'https://www.sphinx-doc.org/en/master/'},
            {'text': 'PyData Theme', 'url': 'https://pydata-sphinx-theme.readthedocs.io/'},
        ]
    },
}
# Ensure html_context is not overwritten
html_context.update({
    "color_scheme": sub_theme,
})

# Add version switcher configuration
html_theme_options["switcher"] = {
    "json_url": "/_static/switcher.json",
    "version_match": sub_theme,
}

