Line wrap for code block
========================

Line wrap for code block is a custom extension that allows you to wrap lines when the text is too long. 

How to use an line wrap extension
---------------------------------
This extension is built in and should affect your code block.

Example of use:

.. code-block::

    # Long line example
    long_string = "This is a very long string that should trigger a horizontal scrollbar in the code block and the button should be visible."

Code for code block above:

.. code-block::

    .. code-block::

    # Long line example
    long_string = "This is a very long string that should trigger a horizontal scrollbar in the code block and the button should be visible."


.. code-block::

    # Not that long line example
    long_string = "This is a string that should NOT trigger scrollbar in the code block."

Code for code block above:
.. code-block::

    .. code-block::

    # Not that long line example
    long_string = "This is a string that should NOT trigger scrollbar in the code block."


