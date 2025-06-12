====
Tabs
====

.. note::

    The tabs component requires the `sphinx-design` extension. 
    Ensure it is installed and enabled in your Sphinx configuration.

.. tab-set::

    .. tab-item:: c++

        .. code-block:: c++

            int main(const int argc, const char **argv) {
                return 0;
            }

    .. tab-item:: python

        .. code-block:: python

            def main():
                return

    .. tab-item:: java

        .. code-block:: java

            class Main {
                public static void main(String[] args) {
                }
            }

    .. tab-item:: julia

        .. code-block:: julia

            function main()
            end

    .. tab-item:: fortran

        .. code-block:: fortran

            PROGRAM main
            END PROGRAM main

Code:
::
    .. tab-set::

        .. tab-item:: c++

            .. code-block:: c++

                int main(const int argc, const char **argv) {
                    return 0;
                }

        .. tab-item:: python

            .. code-block:: python

                def main():
                    return

        .. tab-item:: java

            .. code-block:: java

                class Main {
                    public static void main(String[] args) {
                    }
                }

        .. tab-item:: julia

            .. code-block:: julia

                function main()
                end

        .. tab-item:: fortran

            .. code-block:: fortran

                PROGRAM main
                END PROGRAM main