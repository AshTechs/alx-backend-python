#!/usr/bin/env python3
"""
This module contains a test case for the memoize decorator.
"""

import unittest
from unittest.mock import patch

def memoize(func):
    """
    Memoize decorator to cache the result of a method call.
    """
    cache = {}

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func

class TestClass:
    """
    A test class to demonstrate the memoize decorator.
    """

    def a_method(self) -> int:
        """
        Returns a constant value.
        """
        return 42

    @memoize
    def a_property(self) -> int:
        """
        Returns the result of a_method, memoized.
        """
        return self.a_method()

class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.
    """

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """
        Test that a_property returns the correct result and a_method is called only once.
        """
        test_instance = TestClass()
        self.assertEqual(test_instance.a_property(), 42)
        self.assertEqual(test_instance.a_property(), 42)
        mock_a_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
