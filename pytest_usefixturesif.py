import os
import pytest


def pytest_configure(config):
    """Register the mark pytest.markusefixturesif() to py.test"""
    config.addinivalue_line("markers",
                            "usefixturesif(condition, fixture_name, ...): mark test to use fixtures if condition returns True")


def pytest_runtest_setup(item):
    """Add pytest.markusefixturesif() to py.test"""
    for info in item.iter_markers('usefixturesif'):
        if info.args[0]:
            if isinstance(info.args[1], (list, tuple)):
                item.fixturenames.extend(info.args[1])
            else:
                item.fixturenames.extend(info.args[1:])
