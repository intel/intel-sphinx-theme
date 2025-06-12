Branding and logo
=================

Customize logo and title
------------------------

To use a local image file for the logo, place it in the html_static_path, which is the _static folder located outside of the build directory. Then, update the html_logo configuration to reference the image file.

.. code:: python

   html_static_path = ["_static"]
   html_logo = "logo.png"

For different logos in "light" and "dark" modes, update the `html_theme_options` configuration:

.. code-block:: python

   html_static_path = ["_static"]
   html_theme_options = {
      "logo": {
         "image_light": "logo-light.png",
         "image_dark": "logo-dark.png",
      }
   }

To customize the logo link or add a logo title, modify the `html_theme_options`:

.. code-block:: python

   html_theme_options = {
       "logo": {
           "link": "https://example.com",
           "text": "My awesome documentation",
       }
   }

Add favicons
------------

The intel_sphinx_theme provides a default favicon that automatically switch between light and dark modes based on the user's browser/system preference. You don't need to configure anything to use these defaults.

If you want to override the default favicons, you can use the standard `html_favicon` configuration:

.. code-block:: python

   html_favicon = "_static/my-custom-favicon.svg"  # or .ico, .png

For standard favicons, use the `html_favicon` configuration. To add device-specific favicons, use `html_theme_options["favicons"]`:

.. code-block:: python

   html_theme_options = {
      # ...
      "favicons": [
         {
            "rel": "icon",
            "sizes": "16x16",
            "href": "favicon-16x16.png",
         },
         # more favicons
      ],
      # ...
   }

More logo options can be found in `pydata theme documentation <https://pydata-sphinx-theme.readthedocs.io/en/v0.16.1/>`_.