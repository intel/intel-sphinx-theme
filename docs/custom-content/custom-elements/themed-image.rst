Themed image
=============

Themed image is a custom directive that allows you to add two versions of the same image to your documentation,
one for a dark theme and another for a light theme. This feature ensures that your images are clearly
visible and aesthetically pleasing, regardless of the theme your readers are using.

.. important::
    Use this directive only if you want to have two different images in light and dark mode. If you want to have only one image use `img` directive.

Creating a Themed Image
-----------------------

To properly display themed images, you need to prepare two versions of each image – one for the dark theme and another for the light theme.

1. Create two versions of your image, ensuring that they are optimized for visibility in both light and dark themes.

2. Place images in the appropriate directories, typically with paths like `media/light/image.png`` and `media/dark/image.png`.

3. Place both image files in the specified media directory. In the example above, the media directory is `media`.

The structure of your directory with images should look like this:

::

    images
    ├── dark          
    │   └── dark-image.png
    └── light
        └── light-image.png

.. important::

   Make sure that the basic path you add in themed-image is path to light mode image.

Examples of usage themed image:
-------------------------------

.. code-block::

   .. themed-image:: media/themed-image/light/person.png

This can work with all of image extensions.

.. code-block::

   .. themed-image:: media/themed-image/light/cat.svg

Displaying Themed Images in Your Documentation
----------------------------------------------

Once you've prepared your images and added the `themed-image` directive to your documentation, your images will be displayed according to the reader's theme preference. The light version of the image will be shown when the light theme is active, and the dark version will be displayed when the dark theme is active.

Note: Make sure to rebuild your documentation after making changes to ensure that the themed images are properly displayed.

Example of working themed images
--------------------------------

PNG example:

.. themed-image:: media/themed-image/light/person.png
    
SVG example:

.. themed-image:: media/themed-image/light/cat.svg
    :width: 350
