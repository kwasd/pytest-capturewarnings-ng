from pathlib import Path
WARNINGS_FOUND_LINE = '*Total warnings written to test_warnings.txt: 32*'
WARNINGS_NOT_FOUND_LINE = '*No warnings to write.*'

PYFILE_WITH_WARNINGS = """
    import pytest
    import warnings

    @pytest.mark.parametrize("x", range(0,16))
    def test_hello_world_1(x):
        warnings.warn('warning 1')
        warnings.warn('warning 2')
"""

PYFILE_WITHOUT_WARNINGS = """
    import pytest
    import warnings

    @pytest.mark.parametrize("x", range(0,16))
    def test_hello_world_1(x):
        pass
"""

def test_run_with_warnings(pytester):
    pytester.makepyfile(PYFILE_WITH_WARNINGS)
    result = pytester.runpytest('-v')

    result.stdout.fnmatch_lines([
        WARNINGS_FOUND_LINE,
    ])

    assert result.ret == 0

def test_run_with_warnings_xdist(pytester):
    pytester.makepyfile(PYFILE_WITH_WARNINGS)
    result = pytester.runpytest('-v', '-n', 'auto')

    result.stdout.fnmatch_lines([
        WARNINGS_FOUND_LINE,
    ])

    assert result.ret == 0

def test_run_with_json(pytester):
    pytester.makepyfile(PYFILE_WITH_WARNINGS)
    result = pytester.runpytest('-v', '--warnings-json-output-file', 'output.json')

    import json
    j = json.loads(open(pytester.path.joinpath(('output.json'))).read())

    result.stdout.fnmatch_lines([
        WARNINGS_FOUND_LINE,
    ])

    assert len(j) == 32

    assert result.ret == 0

def test_run_without_warnings(pytester):
    pytester.makepyfile(PYFILE_WITHOUT_WARNINGS)

    result = pytester.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        WARNINGS_NOT_FOUND_LINE,
    ])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_run_without_warnings_xdist(pytester):
    pytester.makepyfile(PYFILE_WITHOUT_WARNINGS)

    result = pytester.runpytest('-v', '-n', 'auto')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        WARNINGS_NOT_FOUND_LINE,
    ])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0

