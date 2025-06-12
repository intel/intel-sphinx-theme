===========
Copybuttons
===========

.. note::

   The copybutton component requires the `sphinx-copybutton` extension. Ensure it is installed and enabled in your Sphinx configuration.

`sphinx-copybutton <https://sphinx-copybutton.readthedocs.io/en/latest/>`__ adds a copy button to each of your code cells.
You can see it in action by hovering over the code cell below:

.. code-block:: python

    print("A copybutton in the top-right!")

.. admonition:: nbsphinx

    If your documentation site uses both nbsphinx and Sphinx-copybutton, you
    will want to add the following line to your ``conf.py`` file to prevent the
    copy button from appearing on top of notebook cell numbers:

    .. code-block:: python
        :caption: conf.py

        copybutton_selector = ":not(.prompt) > div.highlight pre"
