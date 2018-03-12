from setuptools import setup

setup(
    name="humps",
    packages=["humps", "tests"],
    version="0.2.1",
    author="Erik Huizinga",
    author_email="huizinga.erik@gmail.com",
    license='LGPL-3.0',
    url="https://github.com/erikhuizinga/humps",
    description="camelCase converter",
    long_description=
    "*********\n"
    "``humps``\n"
    "*********\n"
    "\n"
    "*Convert any string to camelCase.*\n"
    "\n"
    "camelCase starts with a lower case alphabetic character, the rest of the string contains alphanumeric "
    "characters. Any character case in the input is ignored. Any spaces in the input capitalise the following "
    "character if alphabetic, except for the first character. Any non-alphanumeric characters are ignored.",
    keywords=["camelcase", 'camel', 'case', "string", "conversion"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Text Editors",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
    ],
)
