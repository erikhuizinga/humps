*********
``humps``
*********

*Convert any string to camelCase.*

Description
===========

camelCase starts with a lower case alphabetic character, the rest of the string contains alphanumeric characters. Any character case in the input is ignored. Any spaces in the input capitalise the following character if alphabetic, except for the first character. Any non-alphanumeric characters are ignored.

Installation
============

Shell:

.. code-block:: sh

  pip install humps


Python:

.. code-block:: python

  from humps.camel import case

  print(case('Hello, World!'))
  # Output: helloWorld
