Getting started
===============

Get started with development
----------------------------

This section provides a straightforward guide to initiate local development of this theme, enabling you to contribute effectively.

Steps for Contributing Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We adhere to a `standard GitHub workflow <https://guides.github.com/introduction/flow/>`_ comprising:

- Creating a branch
- Opening a pull request
- Rectifying issues identified by various linters and checks
- Addressing code review feedback

The following sections elaborate on these steps.

Clone the Repository
~~~~~~~~~~~~~~~~~~~~

To begin, obtain your own copy of the `pydata-sphinx-theme` codebase by cloning it for local development:

**Clone the repository locally** to have a working copy on your machine::

    $ git clone https://github.com/intel/intel-sphinx-theme
    $ cd intel-sphinx-theme

Set up Your Tools
~~~~~~~~~~~~~~~~~

Sphinx site building employs a mix of Python and Jinja to manage HTML, SCSS, and Javascript.

Sphinx installation:

- `Sphinx <https://www.sphinx-doc.org/en/master/usage/installation.html>`_

The remaining dependencies can be found in the `requirements.txt` file in `/docs/requirements.txt`. Run the command::

    $ pip install -r requirements.txt
    
from the docs directory to install them.

Build the Documentation and Install the Theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to building the documentation, install the current theme version by executing the::
    
    $ python setup.py install --user

command in the `intel_sphinx_theme` directory.

To build the documentation, navigate to the `docs` directory, ensuring all dependencies are installed. Then, execute the::
    
    $ make.bat html

command in the `docs` directory to build the example documentation.

This will install the required dependencies and build the documentation located in the `docs/` folder, placing the output in the `docs/_build/html` folder. If the documentation has already been built, only updated pages will be rebuilt. You can preview the documentation locally by opening an HTML file from this folder.

Alternatively, use the built-in Python `http.server <https://docs.python.org/3/library/http.server.html#module-http.server>`_ by running::

    $ python -m http.server -d docs/_build/html/

A local URL will be displayed, which you can open in a browser to explore the HTML files.

Modify Content and Rebuild
~~~~~~~~~~~~~~~~~~~~~~~~~~

After building the documentation, edit a source file to observe how the documentation is updated with each new build.

1. **Edit a page**. For instance, add a word or correct a typo on any page.
2. **Rebuild the documentation** using `make.bat html`.

Compile the CSS/JS Assets
~~~~~~~~~~~~~~~~~~~~~~~~~

The theme's source files for CSS are located in `intel_sphinx_theme/intel_sphinx_theme/static`, while those for JS are in `intel_sphinx_theme/intel_sphinx_theme/assets`.

To view the result in the documentation, rebuild the docs once more.