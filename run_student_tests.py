"""
Run file to run all tests in the test directory
"""

import unittest


def main():
    test_loader = unittest.TestLoader()
    tests = test_loader.discover("student_test")
    test_runner = unittest.runner.TextTestRunner()
    result = test_runner.run(tests)
    print('Finished running all tests. Success:',  result.wasSuccessful())


if __name__ == "__main__":
    main()
