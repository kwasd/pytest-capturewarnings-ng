==========================
pytest-capture-warnings-ng
==========================

.. image:: https://img.shields.io/pypi/v/pytest-capture-warnings-ng.svg
    :target: https://pypi.org/project/pytest-capture-warnings-ng
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-capture-warnings-ng.svg
    :target: https://pypi.org/project/pytest-capture-warnings-ng
    :alt: Python versions

.. image:: https://github.com/kwasd/pytest-capture-warnings-ng/actions/workflows/main.yml/badge.svg
    :target: https://github.com/kwasd/pytest-capture-warnings-ng/actions/workflows/main.yml
    :alt: See Build Status on GitHub Actions

A simple xdist compatible plugin to capture warnings into a report file

----

Features
--------


Requirements
------------

* `pytest`


Installation
------------

You can install "pytest-capture-warnings-ng" via `pip`_ from `PyPI`_::

    $ pip install https://github.com/kwasd/pytest-capturewarnings-ng


Usage
-----

  --warnings-output-file=WARNINGS_OUTPUT_FILE
                        Report file to write warnings to (defaults to
                        test_warnings.txt)

The output is written to report file:

    <NODE>: <FSLOCATION>: <WARNING>

Example:

    test_run_with_warnings.py::test_hello_world_1: /tmp/pytest-of-vmusin/pytest-38/popen-gw0/test_run_with_warnings0/test_run_with_warnings.py:5: UserWarning: hello 1 world   warnings.warn('hello 1 world') 



Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `Apache Software License 2.0`_ license, "pytest-capture-warnings-ng" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: https://opensource.org/licenses/MIT
.. _`BSD-3`: https://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: https://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: https://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/kwasd/pytest-capture-warnings-ng/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
