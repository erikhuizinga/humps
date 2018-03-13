# Changelog

All releases contain all previous releases' content, except for the noted new features, changes, deprecations, etc.

## v0.2.2

 - Change module structure, use: `from humps.camel import case`
 - Add CHANGELOG.md
 - Use Twine as setup tool
 - Add shell script to build and upload distribution
   - You may need to install and configure [Twine](https://github.com/pypa/twine), e.g. use its environment variables
 - Extend long package description to match README.rst

## v0.1.0

 - Support conversion of any string to camelCase
 - Raise error for non `str` type inputs
 - Ignore any non-alphanumeric characters
