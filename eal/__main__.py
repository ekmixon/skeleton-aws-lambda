"""Code to run if this package is used as a Python module."""


# Standard Python Libraries
import sys

from .example_aws_lambda import main

if return_code := main():
    sys.exit(return_code)
