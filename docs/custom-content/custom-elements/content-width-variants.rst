Adjusting Content Width
=======================

Content width plays a vital role in the readability and presentation of your documentation. This guide will walk you through the process of setting the content width in your project. Currently, there are three content width options available:

1. Small
2. Medium
3. Large

How to Set the Content Width
-----------------------------

To set the content width in your project, you'll need to modify your `conf.py` file.

Follow these steps:

1. Locate the `conf.py` file in your project directory.

2. Open the file in your preferred text editor.

3. Add or modify the `html_context` dictionary to include the `content_width` key with the desired content width value (either "small", "medium", or "large").

For example, to set the content width to medium, your `html_context` dictionary should look like this:

.. code-block:: python

   html_context = {
      # ...
      "content_width": "medium",
      # ...
   }

4. Save the changes to your `conf.py` file.

5. Rebuild your documentation to apply the new content width setting.

Now, your chosen content width should be applied to your project's documentation, providing an optimal reading experience for your users.

Remember that you can always change the content width setting as needed by updating the `content_width` key in the `html_context` dictionary and rebuilding your documentation.