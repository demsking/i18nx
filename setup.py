# pylint: disable=missing-module-docstring

from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
  readme = f.read()

setup(
  name = 'i18nx',
  version = '1.1.0',
  description="Lightweight i18n for Python",
  long_description = readme,
  long_description_content_type = 'text/markdown',
  keywords = ['i18n', 'internationalization', 'translate'],
  readme='README.md',
  python_requires='>=3.9',
  license = 'MIT',
  packages = find_packages(exclude=['tests*']),
  author = 'Sébastien Demanou',
  author_email = 'demsking@gmail.com',
  url = 'https://gitlab.com/demsking/i18nx',
  install_requires = [],
  py_modules = [
    'i18nx',
  ],
)
