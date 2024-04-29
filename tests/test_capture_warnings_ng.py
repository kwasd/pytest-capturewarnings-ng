

def test_help_message(pytester):
    result = pytester.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'capture-warnings-ng:',
        '*--foo=DEST_FOO*Set the value for the fixture "bar".',
    ])


def test_hello_ini_setting(pytester):
    pytester.makeini("""
        [pytest]
        HELLO = world
    """)

    pytester.makepyfile("""
        import pytest
        import warnings

        @pytest.fixture
        def hello(request):
            warnings.warn('hello 1 world')
            return request.config.getini('HELLO')

        def test_hello_world(hello):
            warnings.warn('hello 2 world')
            assert hello == 'world'
    """)

    result = pytester.runpytest('-v')

    # fnmatch_lines does an assertion internally
    #result.stdout.fnmatch_lines([
    #    '*Total warnings: 2*',
    #])

    # make sure that we get a '0' exit code for the testsuite
    assert result.ret == 0
