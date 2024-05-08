import pytest
import pdb

def pytest_addoption(parser):
    parser.addoption("--warnings-output-file", action='store', default="test_warnings.txt", 
                     help="Report file to write warnings to (defaults to test_warnings.txt)")

def warnings_output_file(config):
    return config.getoption("--warnings-output-file")
    
#@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_terminal_summary(terminalreporter, config):
    output_file = warnings_output_file(config)
    stats_warnings = terminalreporter.stats.get('warnings', [])
    if len(stats_warnings) == 0: 
        print(f"No warnings to write.")
    if len(stats_warnings) > 0:
        with open(output_file, "w") as f:
            for w in stats_warnings:
                #location = ":".join(map(str, w.fslocation))
                message = " @ ".join([w.nodeid, w.message]).replace("\n", " ")
                f.write(f"{message}\n")
        print(f"Total warnings written to {output_file}: {len(stats_warnings)}")

#def pytest_collectreport(report):
#    pdb.set_trace()
#    print("COLLECT REPORT")
#    print(report)
