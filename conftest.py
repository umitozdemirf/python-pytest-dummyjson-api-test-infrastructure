"""Configuration for pytest runner."""

import pytest
import os

pytest_plugins = 'pytester'


@pytest.fixture(scope='session')
def run_services():
    """Run services for tests."""
    return True

