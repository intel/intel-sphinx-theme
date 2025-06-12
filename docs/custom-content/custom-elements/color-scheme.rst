Color scheme
============

This documentation page will guide you through the process of using different color schemes in your project. Currently, there are two color schemes available:

1. Intel brand (default)
2. Intel Tiber

.. list-table:: Primary colors in color schemes
   :header-rows: 1

   * - Intel brand
     - Tiber
   * - .. raw:: html

         Light mode: <div style="margin-left:1rem; display:inline-block; background-color:#0054ae; width:15px; height:15px;"></div><br/>
       
       .. raw:: html

         Dark mode: <div style="margin-left:1.24rem; display:inline-block; background-color:#00c7fd; width:15px; height:15px;"></div>
     - .. raw:: html

         Light mode: <div style="margin-left:1rem; display:inline-block; background-color:#5400C0; width:15px; height:15px;"></div><br/>
       
       .. raw:: html

         Dark mode: <div style="margin-left:1.24rem; display:inline-block; background-color:#16CFB1; width:15px; height:15px;"></div>

Visual Examples of documentation using color schemes
----------------------------------------------------

Below are visual examples of the color schemes using every header variant, to see how to use header variants click here :doc:`./header-variants`

.. note::
   To see how it looks like in another mode switch it in top right corner

**Intel brand - default header:**

.. themed-image:: media/color-scheme/light/brand-default.png

**Intel brand - spark-colors header:**

.. themed-image:: media/color-scheme/light/brand-color.png

**Intel brand - spark-squares header:**

.. themed-image:: media/color-scheme/light/brand-squares.png

**Intel Tiber - default header:**

.. themed-image:: media/color-scheme/light/tb-default.png

**Intel Tiber - spark-colors header:**

.. themed-image:: media/color-scheme/light/tb-color.png

**Intel Tiber - spark-squares header:**

.. themed-image:: media/color-scheme/light/tb-squares.png


How to Use a color scheme
---------------------------

To use one of the color scheme in your project, you'll need to modify your `conf.py` file.

Follow these steps:

1. Locate the `conf.py` file in your project directory.

2. Open the file in your preferred text editor.

3. Add or modify the `html_context` dictionary to include the `color_schene` key with the desired color scheme value (either "default" or "tb").

For example, to use the tiber color scheme, your `html_context` dictionary should look like this:

.. code-block:: python

   html_context = {
      # ...
      "color_scheme": "tb",
      # ...
   }

4. Save the changes to your `conf.py` file.

5. Rebuild your documentation to apply the new color scheme.

Now, your chosen color scheme should be applied to your project's documentation.