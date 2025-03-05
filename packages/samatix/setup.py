from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Machine Learning for Asset Managers',
    ext_modules=cythonize("src/runner/pipeline.pyx"),
    zip_safe=False,
)
