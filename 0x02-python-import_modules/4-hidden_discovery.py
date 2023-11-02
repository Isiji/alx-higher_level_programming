#!/usr/bin/bash
__name__ = '__main__':

import py_compile
import sys

# Load the compiled module hidden_4.pyc
try:
    py_compile.compile("hidden_4.pyc")
except Exception:
    sys.exit(1)

# Get the names defined in the module
import hidden_4

# Filter and sort the names
names = [name for name in dir(hidden_4) if not name.startswith("__")]
names.sort()

# Print the names one per line
for name in names:
    print(name)

