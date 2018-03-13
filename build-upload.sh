#!/usr/bin/env bash

rm -rf dist

python setup.py clean check sdist bdist_wheel --universal

gpg --detach-sign -a dist/*.whl
gpg --detach-sign -a dist/*.tar.gz

twine upload dist/*
