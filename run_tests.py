#!/usr/bin/env python3
"""
Simple test runner script.
"""

import subprocess
import sys


def run_command(cmd):
    """Run shell command."""
    print(f"\nRunning: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0


def main():
    """Main function."""
    print("=== Airport Gap Test Framework ===\n")
    
    print("Installing dependencies...")
    if not run_command("pip install -r requirements.txt"):
        print("Failed to install dependencies")
        return 1
    
    print("\nRunning all tests with Allure reporting...")
    if run_command("pytest tests/ --alluredir=allure-results -v"):
        print("All tests passed!")
        print("\nTo view Allure report, run: allure serve allure-results")
        return 0
    else:
        print("Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
