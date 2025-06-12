Buttons
=======

.. note::
   The button component requires the `sphinx-design` extension. Ensure it is installed and enabled in your Sphinx configuration.

Button Groups
=============

Button groups are used to group buttons together. They can be used to group buttons that are related to each other or to group buttons that are part of the same action.

Left-aligned button groups
--------------------------

When the button group is left aligned, the action button should appear to the left of the secondary action.

.. grid:: auto

    .. grid-item::

        .. button-link:: #
            :color: primary
            :tooltip: Action

            Primary action

    .. grid-item::

        .. button-link:: #
            :color: primary
            :outline:
            :tooltip: Secondary Action

            Secondary Action

Right-aligned button groups
---------------------------

When the button group is right aligned, the action button should appear to the right of the secondary action.

.. grid:: auto

    .. grid-item::

        .. button-link:: #
            :color: primary
            :outline:
            :tooltip: Secondary Action

            Secondary Action

    .. grid-item::

        .. button-link:: #
            :color: primary
            :tooltip: Action

            Primary action

Button groups with destructive actions
--------------------------------------

Whenever the action is destructive, the destructive action should be secondary to the cancel action. The destructive button should use the danger button variant.

.. grid:: auto

    .. grid-item::

        .. button-link:: #
            :color: primary
            :tooltip: Cancel

            Cancel

    .. grid-item::

        .. button-link:: #
            :color: danger
            :outline:
            :tooltip: Delete database cannot be undone

            Delete database

Button Variants
===============

.. _button-variants:

.. grid:: auto

    .. grid-item::

        .. button-link:: #
            :color: primary
            :shadow:

            Primary

    .. grid-item::

        .. button-link:: #
            :color: primary
            :outline:
            :shadow:

            Secondary

    .. grid-item::

        .. button-link:: #
            :color: secondary
            :outline:
            :shadow:

            Accent

    .. grid-item::

        .. button-link:: #
            :color: success
            :shadow:

            Success

    .. grid-item::

        .. button-link:: #
            :color: warning
            :shadow:

            Warning

    .. grid-item::

        .. button-link:: #
            :color: danger
            :shadow:

            Danger

    .. grid-item::

        .. button-link:: #
            :color: muted
            :shadow:

            Muted

    .. grid-item::

        .. button-link:: #
            :color: light
            :shadow:

            Light

    .. grid-item::

        .. button-link:: #
            :color: dark
            :shadow:

            Dark

Primary Button
--------------

.. tip:: The primary button is always the filled variant of the primary button. The outline variant is considered to be the secondary button.
.. button-link:: #
   :color: primary
   :tooltip: Primary Button

   Primary Button

.. code-block:: rst

   .. button-link:: #
      :color: primary
      :tooltip: Primary Button

      Primary Button

Secondary Button
----------------

.. tip:: The secondary button is always the outlined variant of the primary button. It does not have a filled version.

.. button-link:: #
   :color: primary
   :outline:
   :tooltip: Secondary Button (Primary Outlined)

   Secondary Button (Primary Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: primary
      :outline:
      :tooltip: Secondary Button (Primary Outlined)

      Secondary Button (Primary Outlined)

Accent Button
-------------
.. warning:: The accent button should be used sparingly.

.. button-link:: #
   :color: secondary
   :tooltip: Accent Button

   Accent Button

.. button-link:: #
   :color: secondary
   :outline:
   :tooltip: Accent Button (Outlined)

   Accent Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: secondary
      :tooltip: Accent Button

      Accent Button

   .. button-link:: #
      :color: secondary
      :outline:
      :tooltip: Accent Button (Outlined)

      Accent Button (Outlined)

Success Button
--------------

.. button-link:: #
   :color: success
   :tooltip: Success Button

   Success Button

.. button-link:: #
   :color: success
   :outline:
   :tooltip: Success Button (Outlined)

   Success Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: success
      :tooltip: Success Button

      Success Button

   .. button-link:: #
      :color: success
      :outline:
      :tooltip: Success Button (Outlined)

      Success Button (Outlined)

Danger Button
-------------

.. button-link:: #
   :color: danger
   :tooltip: Danger Button

   Danger Button

.. button-link:: #
   :color: danger
   :outline:
   :tooltip: Danger Button (Outlined)

   Danger Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: danger
      :tooltip: Danger Button

      Danger Button

   .. button-link:: #
      :color: danger
      :outline:
      :tooltip: Danger Button (Outlined)

      Danger Button (Outlined)

Warning Button
--------------

.. button-link:: #
   :color: warning
   :tooltip: Warning Button

   Warning Button

.. button-link:: #
   :color: warning
   :outline:
   :tooltip: Warning Button (Outlined)

   Warning Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: warning
      :tooltip: Warning Button

      Warning Button

   .. button-link:: #
      :color: warning
      :outline:
      :tooltip: Warning Button (Outlined)

      Warning Button (Outlined)

Light Button
------------

.. button-link:: #
   :color: light
   :tooltip: Light Button

   Light Button

.. button-link:: #
   :color: light
   :outline:
   :tooltip: Light Button (Outlined)

   Light Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: light
      :tooltip: Light Button

      Light Button

   .. button-link:: #
      :color: light
      :outline:
      :tooltip: Light Button (Outlined)

      Light Button (Outlined)

Dark Button
-----------

.. button-link:: #
   :color: dark
   :tooltip: Dark Button

   Dark Button

.. button-link:: #
   :color: dark
   :outline:
   :tooltip: Dark Button (Outlined)

   Dark Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: dark
      :tooltip: Dark Button

      Dark Button

   .. button-link:: #
      :color: dark
      :outline:
      :tooltip: Dark Button (Outlined)

      Dark Button (Outlined)

Muted Button
------------

.. button-link:: #
   :color: muted
   :tooltip: Muted Button

   Muted Button

.. button-link:: #
   :color: muted
   :outline:
   :tooltip: Muted Button (Outlined)

   Muted Button (Outlined)

.. code-block:: rst

   .. button-link:: #
      :color: muted
      :tooltip: Muted Button

      Muted Button

   .. button-link:: #
      :color: muted
      :outline:
      :tooltip: Muted Button (Outlined)

      Muted Button (Outlined)

Accessibility Note
-----------------

.. note:: Accessibility considerations
   `Sphinx Design buttons
   <https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html>`__
   are actually links, meaning they are rendered in HTML with ``<a>`` tags
   instead of ``<button>``. Use them if you need a link to look like a button,
   however, be aware that they do not follow accessibility best practices for
   native button components such as using the correct `ARIA attributes
   <https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/button_role>`__.
