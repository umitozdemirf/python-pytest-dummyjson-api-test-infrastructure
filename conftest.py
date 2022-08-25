"""Configuration for pytest runner."""

import pytest

from py.xml import html
from config.base_config import BaseConfig

pytest_plugins = 'pytester'


@pytest.fixture(scope='session')
def run_services():
    """Run services for tests."""
    return True


def pytest_html_report_title(report):
    report.title = "Firefly Mobile App Test Recording"


def pytest_configure(config):
    config._metadata["env"] = BaseConfig.env
    config._metadata["Base URL"] = BaseConfig.API_URL
