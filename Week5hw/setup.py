
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="reverse_str",
    ext_modules=cythonize("reverse_str.pyx", language_level=3),
    zip_safe=False,
)
