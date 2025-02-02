from setuptools import setup, find_packages

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from compare_locales import version

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf-8')

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Localization
Topic :: Software Development :: Testing\
"""

setup(name="compare-locales",
      version=version,
      author="Axel Hecht",
      author_email="axel@mozilla.com",
      description='Lint Mozilla localizations',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license="MPL 2.0",
      classifiers=CLASSIFIERS.split("\n"),
      platforms=["any"],
      python_requires='>=3.7, <4',
      entry_points={
        'console_scripts':
        [
            'compare-locales = compare_locales.commands:CompareLocales.call',
            'moz-l10n-lint = compare_locales.lint.cli:main',
        ],
      },
      packages=find_packages(),
      package_data={
          'compare_locales.tests': ['data/*.properties', 'data/*.dtd']
      },
      install_requires=[
          'fluent.syntax >=0.18.0, <0.19',
          'six',  # undeclared dependency of fluent-syntax 0.18.1
          'toml',
      ],
      tests_require=[
          'mock<4.0',
      ],
      test_suite='compare_locales.tests')
