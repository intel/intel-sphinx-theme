=====
Cards
=====

.. note::

    The card component requires the `sphinx-design` extension. 
    Ensure it is installed and enabled in your Sphinx configuration.

Example Set 1
============

.. grid:: auto

    .. grid-item-card:: Only heading

    .. grid-item-card::

        Only body.

        But with multiple text paragraphs.

    .. grid-item-card:: Heading and body

        Content of the third card.

        :bdg-primary:`Sample badge`

Example Set 2
============
.. grid:: auto

    .. grid-item-card:: A card with a dropdown menu

        .. dropdown:: :fa:`eye me-1` Click to expand dropdown

            Hidden content

    .. grid-item-card:: A clickable card
        :link: https://sphinx-design.readthedocs.io/en/pydata-theme/cards.html#clickable-cards
        :link-alt: Clickable cards - Sphinx Design docs

        Don't forget to add the alternative text with ``link-alt``!

Code:
:: 
    .. grid:: auto

        .. grid-item-card:: Only heading

        .. grid-item-card::

            Only body.

            But with multiple text paragraphs.

        .. grid-item-card:: Heading and body

            Content of the third card.

            :bdg-primary:`Sample badge`

Example Set 3
============

.. grid:: auto

    .. grid-item-card:: A card with a dropdown menu

        .. dropdown:: :fa:`eye me-1` Click to expand dropdown

            Hidden content

    .. grid-item-card:: A clickable card
        :link: https://sphinx-design.readthedocs.io/en/pydata-theme/cards.html#clickable-cards
        :link-alt: Clickable cards - Sphinx Design docs

        Don't forget to add the alternative text with ``link-alt``!

Code:
::
    .. grid:: auto

        .. grid-item-card:: A card with a dropdown menu

            .. dropdown:: :fa:`eye me-1` Click to expand dropdown

                Hidden content

        .. grid-item-card:: A clickable card
            :link: https://sphinx-design.readthedocs.io/en/pydata-theme/cards.html#clickable-cards
            :link-alt: Clickable cards - Sphinx Design docs

            Don't forget to add the alternative text with ``link-alt``!

Example Set 4
============
.. grid:: auto

    .. grid-item-card::

        panel 1 header
        ^^^^^^^^^^^^^^
        panel 1 content
        more content
        ++++++++++++++
        panel 1 footer

    .. grid-item-card::

        panel 2 header
        ^^^^^^^^^^^^^^
        panel 2 content
        ++++++++++++++
        panel 2 footer

Code:
::
    .. grid:: auto

        .. grid-item-card::

            panel 1 header
            ^^^^^^^^^^^^^^
            panel 1 content
            more content
            ++++++++++++++
            panel 1 footer

        .. grid-item-card::

            panel 2 header
            ^^^^^^^^^^^^^^
            panel 2 content
            ++++++++++++++
            panel 2 footer