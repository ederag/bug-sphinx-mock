import sys
import os

# The FooClass docstring shows up only if this line is commented out
autodoc_mock_imports = ['bar']

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
