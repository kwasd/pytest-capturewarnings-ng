import pytest
import pdb

def pytest_addoption(parser):
    parser.addoption("--warnings-output-file", action='store', default="test_warnings.txt")

#@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_terminal_summary(terminalreporter):
    print("Hello!")
    #pdb.set_trace()
    warnings = [{field: getattr(w, field) for field in ["message", "fslocation", "nodeid", "get_location"]} for w in terminalreporter.stats['warnings']]
    for w in warnings:
        location = ":".join(map(str, warnings[0]['fslocation']))
        if(w['message'][:len(location)] == location):
           w['message'] = w['message'][len(location)+2:]
    #pdb.set_trace()
    with open("/tmp/warnings.txt", "w") as f:
        for w in warnings:
            f.write(f": {w.message}\n")
    print(f"Total warnings: {len(warnings)}")    

#def pytest_collectreport(report):
#    pdb.set_trace()
#    print("COLLECT REPORT")
#    print(report)
