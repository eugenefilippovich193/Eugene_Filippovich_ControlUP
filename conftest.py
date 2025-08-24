"""
Pytest configuration
"""


def pytest_addoption(parser):
    """Add command line options."""
    parser.addoption("--headless", action="store_true", help="Run in headless mode")
