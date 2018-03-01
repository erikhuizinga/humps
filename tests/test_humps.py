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

import unittest

from ..humps.camel import case


class TestCamel(unittest.TestCase):
    def test_camel(self):
        bad_inputs = {0, str, object, None}

        for bad_input in bad_inputs:
            with self.assertRaises(AssertionError):
                case(bad_input)

        input_string_expected = {
            '': '',
            ' ': '',
            ' ' * 1337: '',
            '\\': '',
            '\'': '',
            '\"': '',
            '\a': '',
            '\b': '',
            '\f': '',
            '\n': '',
            '\r': '',
            '\t': '',
            '\v': '',
            '\042': '',  # ASCII \042 := '*' := the answer to life, the universe and everything
            '\x2A': '',  # HEX \x2A := '*'
            '0': '',
            '1 ': '',
            ' 2': '',
            '3 4': '',
            ' 5678  901 234 ': '',
            '5a': 'a',
            '6b c': 'bC',
            '7d8 e': 'd8E',
            '9f0 1g': 'f01G',
            '2h 34i': 'h34I',
            '5j 6k7': 'j6K7',
            'l m89': 'lM89',
            'n': 'n',
            'O': 'o',
            'pQ': 'pq',
            'Rs': 'rs',
            'TU': 'tu',
            'v w': 'vW',
            '  X Y  z   ': 'xYZ',
            'Hello, World!': 'helloWorld',
        }

        for input_string, expected in input_string_expected.items():
            self.assertEqual(expected, case(input_string))


if __name__ == '__main__':
    unittest.main()
