import logging

import pytest


@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    out = yield
    res = out.get_result()
    if res.when == "call":
        logging.info(f"test case id:{res.nodeid}")
        logging.info(f"test result:{res.outcome}")
        logging.info(f"test duration: {res.duration}")