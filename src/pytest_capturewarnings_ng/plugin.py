import pytest
import pdb

def pytest_addoption(parser):
    parser.addoption("--warnings-output-file", action='store', default="test_warnings.txt", 
                     help="Report file to write warnings to (defaults to test_warnings.txt)")
    parser.addoption("--warnings-json-output-file", action='store', default=None, 
                     help="Report JSON file to write warnings to (default: None)")

def warnings_output_file(config):
    return config.getoption("--warnings-output-file")

def warnings_json_output_file(config):
    return config.getoption("--warnings-json-output-file")
    
#@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_terminal_summary(terminalreporter, config):
    text_output_file = warnings_output_file(config)
    json_output_file = warnings_json_output_file(config)
    stats_warnings = terminalreporter.stats.get('warnings', [])
    if len(stats_warnings) == 0: 
        print(f"No warnings to write.")
    if len(stats_warnings) > 0:
        if text_output_file:
            with open(text_output_file, "w") as f:
                for w in stats_warnings:
                    #location = ":".join(map(str, w.fslocation))
                    message = " @ ".join([w.nodeid, w.message]).replace("\n", " ")
                    f.write(f"{message}\n")
        if json_output_file is not None:
            import json
            warnings_list = [{w.nodeid: w.message} for w in stats_warnings]
            with open(json_output_file, 'w') as f:
                f.write(json.dumps(warnings_list))
        print(f"Total warnings written to {text_output_file}: {len(stats_warnings)}")

#def pytest_collectreport(report):
#    pdb.set_trace()
#    print("COLLECT REPORT")
#    print(report)
