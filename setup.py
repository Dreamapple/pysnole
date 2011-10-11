#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name = "pyqterm",
        version = "0.1",
        summary="Simple terminal/console widget for PyQt4 with vt100 support",
        author="Henning Schroeder",
        author_email="henning.schroeder@gmail.com",
        packages = find_packages(),
    )
