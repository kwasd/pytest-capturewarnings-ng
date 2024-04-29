
WARNINGS_FOUND_LINE = '*Total warnings written to test_warnings.txt: 2*'
WARNINGS_NOT_FOUND_LINE = '*No warnings to write.*'

# def test_help_message(pytester):
#     result = pytester.runpytest(
#         '--help',
#     )
#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         'capture-warnings-ng:',
#         '*--foo=DEST_FOO*Set the value for the fixture "bar".',
#     ])


def test_run_with_warnings(pytester):
    pytester.makepyfile("""
        import pytest
        import warnings

        def test_hello_world_1(request):
            warnings.warn('hello 1 world')

        def test_hello_world_2(request):
            warnings.warn('hello 2 world')
    """)

    result = pytester.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        WARNINGS_FOUND_LINE,
    ])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0

def test_run_without_warnings(pytester):
    pytester.makepyfile("""
        import pytest
        import warnings

        def test_hello_world_1(request):
            pass

        def test_hello_world_2(request):
            pass
    """)

    result = pytester.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        WARNINGS_NOT_FOUND_LINE,
    ])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0

def test_run_xdist_with_warnings(pytester):
    pytester.makepyfile("""
        import pytest
        import warnings

        def test_hello_world_1(request):
            warnings.warn('hello 1 world')

        def test_hello_world_2(request):
            warnings.warn('hello 2 world')
    """)

    result = pytester.runpytest('-v', '-n', 'auto')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        WARNINGS_FOUND_LINE,
    ])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0

def test_run_xdist_without_warnings(pytester):
    pytester.makepyfile("""
        import pytest
        import warnings

        def test_hello_world_1(request):
            pass

        def test_hello_world_2(request):
            pass
    """)

    result = pytester.runpytest('-v', '-n', 'auto')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        WARNINGS_NOT_FOUND_LINE,
    ])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0

