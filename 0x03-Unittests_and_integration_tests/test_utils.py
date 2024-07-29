#!/usr/bin/env python3
"""
Unit tests for the memoize decorator to verify caching behavior.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator.
    """

    class TestClass:
        """
        TestClass is used to demonstrate memoization with the memoize decorator.
        """

        def a_method(self):
            """
            A simple method that returns a constant value.

            Returns:
            int: A constant value of 42.
            """
            return 42

        @memoize
        def a_property(self):
            """
            A property method decorated with memoize.

            Returns:
            int: The result of calling a_method.
            """
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """
        Test that a_property returns the correct result and a_method is called only once.

        Parameters:
        mock_a_method (Mock): The mocked a_method to control its return value.
        """
        test_instance = self.TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Check that the result is correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Check that a_method was called only once
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
