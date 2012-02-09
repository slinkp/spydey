from setuptools import setup, find_packages
import sys, os

version = '0.5'


def get_usage():
    try:
        from spydey.spider import get_optparser
    except ImportError:
        return '\n'
    parser = get_optparser()
    parser.prog = 'spydey'
    usage = parser.format_help()
    # Add some indentation for using as ReStructured Text code block.
    usage = usage.replace('\n', '\n ')
    usage = '\nUsage\n=======\n\n::\n\n ' + usage
    return usage

here = os.path.dirname(__file__)
README = open(os.path.join(here, 'README.txt')).read()
README += get_usage()
README += open(os.path.join(here, 'CHANGES.txt')).read()

setup(name='spydey',
      version=version,
      description="A simple web spider with pluggable recursion strategies",
      long_description=README,
      classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Paul M. Winkler',
      author_email='slinkp@gmail.com',
      url='http://github.com/slinkp/spydey',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
        'httplib2',
        'lxml',

      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      spydey=spydey.spider:main
      """,
      )
