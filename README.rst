=======
Spydey
=======

A simple web spider with several recursion strategies.
Home page is at http://github.com/slinkp/spydey.

It doesn't do much except follow links and report status.  I mostly
use it for quick and dirty smoke testing and link checking.

**************
Quick start
**************

For lazy, zero-configuration smoke testing, I typically run it like::

  spydey -r -p --stop-on-error --max-requests=200 --traversal=pattern --profile --log-referrer URL


For more options see the ``--help``.

****************
Installation
****************

Any of the standard python install tools should work;
eg ``pip install spydey`` will install the latest from pypi.

***********
Features
***********

Many of the command-line options are shamelessly stolen from `wget`.

Traversal
===========

The most unusual feature is the ``--traversal`` option, which allows specifying
how the spider decides which page to crawl next.
The novel (I think?) option
is ``--traversal=pattern``, which tries to recognize patterns of site hierarchy
in URLs, and will follow URLs of novel patterns before those with patterns it
has seen before.  When there are no novel patterns to follow, it follows random
links to URLs of known patterns. If you use this for smoke-testing a typical
modern web app that maps URL patterns to views or controllers, this will very
quickly hit all your views/controllers at least once... usually.  The goal here
is to most quickly find what's broken!
I got tired of using tools like ``wget`` and waiting for downloading eg
thousands and thousands of user profiles before trying a single comment form.

``--traversal=pattern`` is less
interesting when pointed at a website that has arbitrarily deep trees (static
files, VCS repositories, and the like).

The other options are:

- random: what it sounds like.
- breadth-first: explores all known siblings before going deeper.
- depth-first: goes deep before exploring siblings.
- hybrid: this alternates between depth-first and breadth-first behavior.
  When is this useful? Possibly never, I just wanted to try it.

Also, Spydey is designed so that adding a new recursion strategy is
trivial. Part of the motivation was to allow me to experiment with different
recursive crawling strategies. Read the source.

Colored output
=================

Requires installing the optional ``fabulous`` library.

Profiling
============

This just measures the time to fetch each page and then summarizes
the slowest ones at the end::

  spydey -r -p --profile  https://slinkp.com
  INFO:spydey:1. 200 https://slinkp.com  (0.085 secs)
  INFO:spydey:2. 200 https://slinkp.com/feeds/all.atom.xml  (0.073 secs)
  ...

  Slowest 20 URLs:
  [(0.0914008617401123,
  'https://slinkp.com/sisyphus_pygotham_2014/static/problem_solved.gif'),
  (0.07724189758300781, 'https://slinkp.com/emacs/lsp-find-definition-peek.gif'),
  (0.058413028717041016, 'https://slinkp.com/emacs/lsp-breadcrumbs.gif'),
  (0.057930946350097656,
  'https://slinkp.com/emacs/lsp-find-references-peek.gif'),
  (0.05424308776855469, 'https://slinkp.com'),
  (0.053025007247924805,
  'https://slinkp.com/sisyphus_pygotham_2014/static/whsyh0b.gif'),
  ...


***************
Development
***************

To build a new distribution:

- Bump the version number in ``spydey/__init__.py``
- Add an entry to the top of ``CHANGES.txt``

Make sure we have the latest tools::

  python3 -m pip install --upgrade twine pip setuptools wheel``

Build a distribution::

  python3 -m build --sdist .

Check the built distribution::

  twine check dist/*

Upload it::

  twine upload dist/*
