import os
import datetime
from .themed_image import ThemedImage
from .link_list import LinkList
from sphinx.util import logging
from sphinx.util.fileutil import copy_asset
from docutils import nodes

logger = logging.getLogger(__name__)

def copy_themed_images(app, env):
    for docname in env.found_docs:
        doctree = env.get_doctree(docname)
        for node in doctree.traverse(nodes.image):
            if 'themed-image-container' in node.get('classes', []):
                uri = node['uri']
                source = os.path.join(app.srcdir, uri)
                dest = os.path.join(app.outdir, '_images', os.path.basename(uri))
                copy_asset(source, dest)
                logger.info(f'copied themed image: {uri}', color='green')

def _add_to_context(app, pagename, templatename, context, doctree):
    # Add current year to context for copyright
    context['current_year'] = datetime.datetime.now().year
    
    # Handle favicon configuration
    # If user has defined html_favicon, don't override it
    if not hasattr(app.config, 'html_favicon') or app.config.html_favicon is None:
        # Use our default favicon - will be handled by template based on color scheme
        context['theme_default_favicon'] = True

def get_theme_path():
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return theme_path

def setup(app):
    theme_path = get_theme_path()
    templates_path = os.path.join(theme_path, 'templates')
    app.config.templates_path.append(templates_path)
    static_path = os.path.join(theme_path, 'static')
    app.config.html_static_path.append(static_path)
    app.add_html_theme('intel_sphinx_theme', theme_path)
    app.add_directive("themed-image", ThemedImage)
    app.add_directive('link-list', LinkList)
    app.connect('env-updated', copy_themed_images)
    app.connect('html-page-context', _add_to_context)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
