#!/bin/bash

# Project Folders
FOLDER="src"

# Run Tools
isort $FOLDER -c --diff
black --check --diff --skip-string-normalization $FOLDER
pycodestyle $FOLDER
flake8 $FOLDER
mypy $FOLDER
