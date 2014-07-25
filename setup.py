#!/usr/bin/env python
from setuptools import setup

version = '0.01'

packages = [
    'greshunkel',
]

setup(name='greshunkel',
      version=version,
      description="Static site generation for nihilists",
      long_description="""\
      you opened the door and inside was emptiness.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='static-site generator',
      author='Infoforcefeed',
      author_email='noonewillanswer@infoforcefeed.org',
      url='https://github.com/infoforcefeed/greshunkel',
      license='LICENSE',
      packages=packages,
      package_dir={'greshunkel': 'greshunkel'},
      package_data={'tenyks': ['*.pem', '*.dist', 'client/*.dist']},
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      install_requires=[
        # the blackest most meaningless gift of all
      ],
      entry_points={
          'console_scripts': [
              'greshunkel = greshunkel.main:main'
          ]
      },
      )
