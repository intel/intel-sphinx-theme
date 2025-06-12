Header Variants
===============

This documentation page will guide you through the process of using different header variants in your project. Currently, there are three header variants available:

1. Spark color
2. Spark squares
3. Default

Visual Examples of Header Variants
----------------------------------

Below are visual examples of the three header variants:

.. note::
   To see how it looks like in another mode switch it in top right corner

**Spark color:**

.. themed-image:: media/header-variants/light/spark-color.png

**Spark squares:**

.. themed-image:: media/header-variants/light/spark-squares.png

**Default:**

.. themed-image:: media/header-variants/light/default.png

How to Use a Header Variant
---------------------------

To use one of the header variants in your project, you'll need to modify your `conf.py` file.

Follow these steps:

1. Locate the `conf.py` file in your project directory.

2. Open the file in your preferred text editor.

3. Add or modify the `html_context` dictionary to include the `header_variant` key with the desired header variant value (either "spark-color", "spark-squares", or "default").

For example, to use the spark color header variant, your `html_context` dictionary should look like this:

.. code-block:: python

   html_context = {
      # ...
      "header_variant": "spark-color",
      # ...
   }

4. Save the changes to your `conf.py` file.

5. Rebuild your documentation to apply the new header variant.

Now, your chosen header variant should be applied to your project's documentation.