Link List
=========

The Link List is a custom directive that allows you to add a list of links to your documentation.

Types of Link Lists
-------------------
There are two types of link lists you can use in your documentation:

1. **Global Link List**: This appears in the right sidebar of the entire documentation.
2. **Page-Oriented Link List**: This appears at a specific location within a particular page.

Global Link List
----------------
To add a global link list, you need to define it in the ``conf.py`` file under the ``html_context``. The configuration allows you to specify a title for the list and the links themselves.

**Example**:

In the ``conf.py`` file:

.. code-block:: python

   html_context = {
       # ...
       'global_link_list': {
           'title': 'Created with',
           'links': [
               {'text': 'Sphinx', 'url': 'https://www.sphinx-doc.org/en/master/'},
               {'text': 'PyData Theme', 'url': 'https://pydata-sphinx-theme.readthedocs.io/'},
           ]
       }
       # ...
   }

This will display a list of links in the right sidebar across your documentation.

Page-Oriented Link List
-----------------------
To add a page-oriented link list, use the ``link-list`` directive directly within the page where you want the list to appear. You can specify the title of the link list and the links.

**Example**:

.. code-block:: rst

   .. link-list::
      :title: Resources

      Sphinx Documentation https://www.sphinx-doc.org/en/master/
      Python https://www.python.org/
      PyData Theme https://pydata-sphinx-theme.readthedocs.io/

This will insert the list of links in the desired position on the page.

Examples of Link Lists
----------------------

**Global Link List**  
A global link list displays in the sidebar, providing easy access to common resources.

.. themed-image:: media/link-list/light/global-link-list.png

.. |br| raw:: html

    <br />
    
**Page-Oriented Link List**  
The following example shows how a page-oriented link list looks within a page:

.. link-list::
      :title: Resources

      Sphinx Documentation https://www.sphinx-doc.org/en/master/
      Python https://www.python.org/
      PyData Theme https://pydata-sphinx-theme.readthedocs.io/

.. code-block:: rst

   .. link-list::
      :title: Resources

      Sphinx Documentation https://www.sphinx-doc.org/en/master/
      Python https://www.python.org/
      PyData Theme https://pydata-sphinx-theme.readthedocs.io/