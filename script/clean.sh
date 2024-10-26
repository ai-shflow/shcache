#!/bin/bash

chmod 644 .gitignore
chmod 644 Dockerfile LICENSE Makefile MANIFEST.in README.md requirements.txt setup.cfg
chmod 644 cache.py setup.py

find shcache -name "*.py" -exec chmod 644 {} \;
find shcache -name "*.yml" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
