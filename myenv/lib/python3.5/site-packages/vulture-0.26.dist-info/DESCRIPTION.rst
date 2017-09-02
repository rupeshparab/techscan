Vulture - Find dead code
========================

.. image:: https://travis-ci.org/jendrikseipp/vulture.svg?branch=master
   :target: https://travis-ci.org/jendrikseipp/vulture

Vulture finds unused code in Python programs. This is useful for
cleaning up and finding errors in large code bases. If you run Vulture
on both your library and test suite you can find untested code.

Due to Python's dynamic nature, static code analyzers like Vulture are
likely to miss some dead code. Also, code that is only called implicitly
may be reported as unused. Nonetheless, Vulture can be a very helpful
tool for higher code quality.


Features
--------

* fast: static code analysis
* lightweight: only one module
* tested: tests itself and has complete test coverage
* complements pyflakes and has the same output syntax
* sorts unused classes and functions by size with ``--sort-by-size``
* supports Python 2.6, 2.7 and 3.x


Installation
------------

::

  $ pip install vulture  # from PyPI
  $ pip install .        # from cloned repo


Usage
-----

::

  $ vulture myscript.py  # or
  $ python3 -m vulture myscript.py
  $ vulture myscript.py mypackage/
  $ vulture myscript.py mywhitelist.py  # Put false-positives in whitelist.
  $ vulture myscript.py --min-confidence 100  # Only report 100% dead code.

The provided arguments may be Python files or directories. For each
directory Vulture analyzes all contained `*.py` files.

After you have found and deleted dead code, run Vulture again, because
it may discover more dead code.

**Handling false positives**

You can add used code that is reported as unused to a Python module and
add it to the list of scanned paths. We collect whitelists for common
Python modules and packages in ``vulture/whitelists/`` (pull requests
are welcome). If you want to ignore a whole file or directory, use the
``--exclude`` parameter (e.g., ``-exclude *settings.py,docs/``).

**Marking unused variables**

There are situations where you can't just remove unused variables, e.g.,
in tuple assignments or function signatures. Vulture will ignore these
variables if they start with an underscore (e.g., ``_x, y = get_pos()``).

**Minimum confidence**

You can use the ``--min-confidence`` flag to set the minimum confidence
for code to be reported as unused. Use ``--min-confidence 100`` to only
report code that is guaranteed to be unused within the analyzed files.


How does it work?
-----------------

Vulture uses the ``ast`` module to build abstract syntax trees for all
given files. While traversing all syntax trees it records the names of
defined and used objects. Afterwards, it reports the objects which have
been defined, but not used. This analysis ignores scopes and only takes
object names into account.

Vulture also detects unreachable code by looking for code after
``return``, ``break``, ``continue`` and ``raise`` statements, and by
searching for unsatisfiable ``if``- and ``while``-conditions.


Sort by size
------------

When using the ``--sort-by-size`` option, Vulture sorts unused code by
its number of lines. This helps developers prioritize where to look for
dead code first.


Similar programs
----------------

* Vulture can be used together with *pyflakes*
* The *coverage* module can find unused code more reliably, but requires
  all branches of the code to actually be run.


Participate
-----------

Please visit https://github.com/jendrikseipp/vulture to report any
issues or to make pull requests.

* Changelog: `NEWS.rst <https://github.com/jendrikseipp/vulture/blob/master/NEWS.rst>`_
* Roadmap: `TODO.rst <https://github.com/jendrikseipp/vulture/blob/master/TODO.rst>`_


News
====

0.26 (2017-08-28)
-----------------
* Detect ``async`` function definitions (thanks @RJ722).
* Add ``Item.get_report()`` method (thanks @RJ722).
* Move method for finding Python modules out of Vulture class.


0.25 (2017-08-15)
-----------------
* Detect unsatisfiable statements containing ``and``, ``or`` and ``not``.
* Use filenames and line numbers as tie-breakers when sorting by size.
* Store first and last line numbers in Item objects.
* Pass relevant options directly to ``scavenge()`` and ``report()``.


0.24 (2017-08-14)
-----------------
* Detect unsatisfiable ``while``-conditions (thanks @RJ722).
* Detect unsatisfiable ``if``- and ``else``-conditions (thanks @RJ722).
* Handle null bytes in source code.


0.23 (2017-08-10)
-----------------
* Add ``--min-confidence`` flag (thanks @RJ722).


0.22 (2017-08-04)
-----------------
* Detect unreachable code after ``return``, ``break``, ``continue`` and
  ``raise`` (thanks @RJ722).
* Parse all variable and attribute names in new format strings.
* Extend ast whitelist.


0.21 (2017-07-26)
-----------------
* If an unused item is defined multiple times, report it multiple times.
* Make size estimates for function calls more accurate.
* Create wheel files for Vulture (thanks @RJ722).


0.20 (2017-07-26)
-----------------
* Report unused tuple assignments as dead code.
* Report attribute names that have the same names as variables as dead code.
* Let Item class inherit from ``object`` (thanks @RJ722).
* Handle names imported as aliases like all other used variable names.
* Rename Vulture.used_vars to Vulture.used_names.
* Use function for determining which imports to ignore.
* Only try to import each whitelist file once.
* Store used names and used attributes in sets instead of lists.
* Fix estimating the size of code containing ellipses (...).
* Refactor and simplify code.


0.19 (2017-07-20)
-----------------
* Don't ignore `__foo` variable names.
* Use separate methods for determining whether to ignore classes and functions.
* Only try to find a whitelist for each defined import once (thanks @roivanov).
* Fix finding the last child for many types of AST nodes.


0.18 (2017-07-17)
-----------------
* Make `--sort-by-size` faster and more accurate (thanks @RJ722).


0.17 (2017-07-17)
-----------------
* Add `get_unused_code()` method.
* Return with exit code 1 when syntax errors are found or files can't be read.


0.16 (2017-07-12)
-----------------
* Differentiate between unused classes and functions (thanks @RJ722).
* Add --sort-by-size option (thanks @jackric and @RJ722).
* Count imports as used if they are accessed as module attributes.


0.15 (2017-07-04)
-----------------
* Automatically include whitelists based on imported modules (thanks @RJ722).
* Add --version parameter (thanks @RJ722).
* Add appveyor tests for testing on Windows (thanks @RJ722).


0.14 (2017-04-06)
-----------------
* Add stub whitelist file for Python standard library (thanks @RJ722)
* Ignore class names starting with "Test" in "test\_" files (thanks @thisch).
* Ignore "test\_" functions only in "test\_" files.


0.13 (2017-03-06)
-----------------
* Ignore star-imported names since we cannot detect whether they are used.
* Move repository to GitHub.


0.12 (2017-01-05)
-----------------
* Detect unused imports.
* Use tokenize.open() on Python >= 3.2 for reading input files, assume
  UTF-8 encoding on older Python versions.


0.11 (2016-11-27)
-----------------
* Use the system's default encoding when reading files.
* Report syntax errors instead of aborting.


0.10 (2016-07-14)
-----------------
* Detect unused function and method arguments (issue #15).
* Detect unused \*args and \*\*kwargs parameters.
* Change license from GPL to MIT.


0.9 (2016-06-29)
----------------
* Don't flag attributes as unused if they are used as global variables
  in another module (thanks Florian Bruhin).
* Don't consider "True" and "False" variable names.
* Abort with error message when invoked on .pyc files.


0.8.1 (2015-09-28)
------------------
* Fix code for Python 3.


0.8 (2015-09-28)
----------------
* Do not flag names imported with "import as" as dead code (thanks Tom Terrace).


0.7 (2015-09-26)
----------------
* Exit with exitcode 1 if path on commandline can't be found.
* Test vulture with vulture using a whitelist module for false positives.
* Add tests that run vulture as a script.
* Add "python setup.py test" command for running tests.
* Add support for tox.
* Raise test coverage to 100%.
* Remove ez_setup.py.


0.6 (2014-09-06)
----------------
* Ignore function names starting with "test\_".
* Parse variable names in new format strings (e.g. "This is {x}".format(x="nice")).
* Only parse alphanumeric variable names in format strings and ignore types.
* Abort with exit code 1 on syntax errors.
* Support installation under Windows by using setuptools (thanks Reuben Fletcher-Costin).


0.5 (2014-05-09)
----------------
* If dead code is found, exit with 1.


0.4.1 (2013-09-17)
------------------
* Only warn if a path given on the command line cannot be found.


0.4 (2013-06-23)
----------------
* Ignore unused variables starting with an underscore.
* Show warning for syntax errors instead of aborting directly.
* Print warning if a file cannot be found.


0.3 (2012-03-19)
----------------
* Add support for python3
* Report unused attributes
* Find tuple assignments in comprehensions
* Scan files given on the command line even if they don't end with .py


0.2 (2012-03-18)
----------------
* Only format nodes in verbose mode (gives 4x speedup).


0.1 (2012-03-17)
----------------
* First release.


