import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='jsonclasses-sanic',
      version='2.3.1',
      description='JSON Classes integration with sanic.',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Fillmula Inc.',
      author_email='wiosoftvictor@163.com',
      license='MIT',
      packages=find_packages(exclude=("tests")),
      zip_safe=False,
      url='https://github.com/fillmula/jsonclasses-sanic',
      include_package_data=True,
      python_requires='>=3.9',
      install_requires=[])
