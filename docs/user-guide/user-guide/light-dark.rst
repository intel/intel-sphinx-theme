Light and dark themes
#####################

This theme allows you to switch between "dark" and "light" modes using a button in the navigation header. By default, the theme mode is set to "auto", which follows the user's system settings.

Configure default theme mode
----------------------------

To set a different default theme mode, update the `html_context` configuration as follows:

.. code-block:: python

   html_context = {
      # ...
      "default_mode": "light"  # or "dark" or "auto"
   }

Customize the CSS for themes
----------------------------

To customize the CSS for both light and dark themes, use the ``html[data-theme='<THEME>']`` CSS selector.

Define custom JavaScript to react to theme changes
--------------------------------------------------

To run custom JavaScript code when the theme changes, define a JavaScript event hook that reacts to ``data-theme`` changes.

More theme switcher options can be found in `pydata theme documentation <https://pydata-sphinx-theme.readthedocs.io/en/v0.15.4/>`_.