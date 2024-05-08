==========================
pytest-capture-warnings-ng
==========================

.. image:: https://github.com/kwasd/pytest-capturewarnings-ng/actions/workflows/test.yml/badge.svg
    :target: https://github.com/kwasd/pytest-capturewarnings-ng/actions/workflows/test.yml
    :alt: See Build Status on GitHub Actions

A simple xdist compatible plugin to capture warnings into a report file

----

Features
--------

Captures warnings from a test run, outputting it to the report file.

Aims to be xdist-compatible.


Requirements
------------

* `pytest`


Installation
------------

You can install "pytest-capturewarnings-ng" via `pip`_ from `PyPI`_::

    $ pip install git+https://github.com/kwasd/pytest-capturewarnings-ng.git@v1.0


Usage
-----

Try `--help` to see a new option::

  --warnings-output-file WARNINGS_OUTPUT_FILE
                        Report file to write warnings to (defaults to
                        test_warnings.txt)

The output is written to report file::

    <NODE> @ <WARNING>

Example::

    tests.demo/test_1.py::test_hello_world_1[1] @ /home/vmusin/pytest-capturewarnings-ng/tests.demo/test_1.py:7: UserWarning: warning 1   warnings.warn('warning 1') 
    tests.demo/test_1.py::test_hello_world_1[1] @ /home/vmusin/pytest-capturewarnings-ng/tests.demo/test_1.py:9: UserWarning: warning 2   warnings.warn('warning 2') 
    tests.demo/test_1.py::test_hello_world_1[2] @ /home/vmusin/pytest-capturewarnings-ng/tests.demo/test_1.py:7: UserWarning: warning 1   warnings.warn('warning 1') 
    tests.demo/test_1.py::test_hello_world_1[2] @ /home/vmusin/pytest-capturewarnings-ng/tests.demo/test_1.py:9: UserWarning: warning 2   warnings.warn('warning 2')


Contributing
------------
Contributions are very welcome. Tests can be run with `pytest`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `Apache Software License 2.0`_ license, "pytest-capturewarnings-ng" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Apache Software License 2.0`: https://www.apache.org/licenses/LICENSE-2.0
.. _`file an issue`: https://github.com/kwasd/pytest-capturewarnings-ng/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
