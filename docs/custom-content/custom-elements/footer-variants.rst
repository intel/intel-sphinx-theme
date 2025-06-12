Footer Variants
===============

This documentation page will guide you through the process of using different footer variants in your project and customizing the footer links. Currently, there are three footer variants available:

1. Simple
2. Line
3. Default

.. caution::

   Please note that the default footer variant is the PyData default footer, which does not include a section about DNS.
   If you require information about DNS, you may need to customize the footer or refer to external resources.

Visual Examples of Footer Variants
----------------------------------

Below are visual examples of the three footer variants:

.. note::
   To see how it looks like in another mode switch it in top right corner

**Simple:**

.. themed-image:: media/footer-variants/light/simple-footer.png

**Line:**

.. themed-image:: media/footer-variants/light/line-footer.png

**Default:**

.. themed-image:: media/footer-variants/light/default-footer.png

How to Use a Footer Variant
---------------------------

To use one of the footer variants in your project, you'll need to modify your `conf.py` file.

Follow these steps:

1. Locate the `conf.py` file in your project directory.

2. Open the file in your preferred text editor.

3. Add or modify the `html_context` dictionary to include the `footer_variant` key with the desired footer variant value (either "simple", "line", or "default").

For example, to use the simple footer variant, your `html_context` dictionary should look like this:

.. code-block:: python

   html_context = {
      # ...
      "footer_variant": "simple",
      # ...
   }

4. Save the changes to your `conf.py` file.

5. Rebuild your documentation to apply the new footer variant.

Customizing Footer Links
------------------------

You can also customize the footer links, such as the terms of use URL, cookies URL, and privacy URL. These links are optional and can be added or modified in the `html_context` dictionary in the `conf.py` file.

For example, to add custom URLs for terms of use, cookies, and privacy, update your `html_context` dictionary like this:

.. code-block:: python

   html_context = {
      # ...
      'footer_links': [
        ('Terms of Use', 'https://www.intel.com/content/www/us/en/legal/terms-of-use.html'),
        ('Cookies', 'https://www.intel.com/content/www/us/en/privacy/intel-cookie-notice.html'),
        ('Privacy', 'https://www.intel.com/content/www/us/en/privacy/intel-privacy-notice.html'),
      ],
      # ...
   }

If you don't want to include any of these links, simply omit the corresponding key from the `html_context` dictionary.

6. Save the changes to your `conf.py` file.

7. Rebuild your documentation to apply the new footer links.

Now, your chosen footer variant should be applied to your project's documentation, and the footer links should be updated according to your preferences.