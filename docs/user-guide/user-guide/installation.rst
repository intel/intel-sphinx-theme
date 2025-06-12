Installation and usage
======================

How to start a sphinx project
*****************************
To start a Sphinx project, follow these simple steps:

1. Install Sphinx:
^^^^^^^^^^^^^^^^^^
First, ensure you have Python and pip installed on your system. Then, open a terminal or command prompt and run the following command to install Sphinx:

.. code-block:: bash
    
    pip install sphinx

2. Create a project directory:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Choose a location on your computer to create a new directory for your project. Navigate to that location and create a new folder with a name of your choice and navigate into the project directory. For example:

.. code-block:: bash
    
    mkdir my_sphinx_project && cd my_sphinx_project

3. Run the Sphinx quickstart:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To set up the basic structure of your project, run the following command:

.. code-block:: bash

    sphinx-quickstart

This command will prompt you to answer a series of questions about your project, such as project name, author, and project version. It will also generate a conf.py configuration file, an index.rst file, and other necessary files.

4. Build the documentation:
^^^^^^^^^^^^^^^^^^^^^^^^^^^
To generate your documentation in HTML format, use the appropriate command for your operating system:

Linux command:

.. code-block:: bash

    make html

Windows command:

.. code-block:: bash

    make.bat html

This will generate an _build/html directory containing the HTML files for your documentation.

5. View the documentation:
^^^^^^^^^^^^^^^^^^^^^^^^^^
Open the _build/html/index.html file in your web browser to view your project's documentation.

From here, you can customize your project's appearance, add content, and configure settings as needed. To learn more about Sphinx and its features, refer to the official `Sphinx documentation <https://www.sphinx-doc.org/en/master/>`_.

How to install spark sphinx theme
*********************************

1. Install the `intel_sphinx_theme` using `pip`:

.. code-block:: bash

    pip install git+https://github.com/intel/intel-sphinx-theme

If you have ssh key configured you can also install it using this command:

.. code-block:: bash

    pip install git+ssh://github.com/intel/intel-sphinx-theme

2. Update the `html_theme` variable in your `conf.py`:

.. code-block:: python

    html_theme = 'intel_sphinx_theme'
