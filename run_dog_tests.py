"""
Start file to run all tests in the test directory
"""

import unittest


def main():
    test_loader = unittest.TestLoader()
    tests = test_loader.discover("dog_test")
    test_runner = unittest.runner.TextTestRunner()
    results = test_runner.run(tests)
    count = tests.countTestCases()
    failed = results.failures
    errors = results.errors
    print(f"Ran {count} tests, failed {len(failed)} tests, errors {len(errors)}")


if __name__ == "__main__":
    main()
