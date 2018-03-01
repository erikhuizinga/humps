# `humps`

*Convert any string to camelCase.*

## Description

camelCase starts with a lower case alphabetic character, the rest of the string contains alphanumeric characters.
Any character case in the input is ignored.
Any spaces in the input capitalise the following alphabetic character, except for the first alphabetic character.
Any non-alphanumeric characters are ignored.

## Installation

Shell:

```bash
pip install humps
```

Python:

```python
from humps import camel

print(camel('Hello, World!'))
# Output: helloWorld
```
