"""
    camel - Convert any string to Python compatible camelCase

    Copyright (C) 2018  Erik Huizinga (GitHub: erikhuizinga, huizinga.erik@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser Public License for more details.

    You should have received a copy of the GNU Lesser Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def case(string: str) -> str:
    """
    Convert string to camelCase. camelCase starts with a lower case alphabetic character, the rest of the string
    contains alphanumeric characters. Any character case in the input is ignored. Any spaces in the input capitalise
    the following character if alphabetic, except for the first character. Any non-alphanumeric characters are ignored.

    :param string: The input string.
    :return: The input converted to camelCase; empty ('') if there are no valid characters in the input string.
    :raises: AssertionError if the input is not of type str.
    """

    assert isinstance(string, str), 'Input must be of type str'

    first_alphabetic_character_index = -1
    for index, character in enumerate(string):
        if character.isalpha():
            first_alphabetic_character_index = index
            break

    empty = ''

    if first_alphabetic_character_index == -1:
        return empty

    string = string[first_alphabetic_character_index:]

    titled_string_generator = (character for character in string.title() if character.isalnum())

    try:
        return next(titled_string_generator).lower() + empty.join(titled_string_generator)

    except StopIteration:
        return empty
