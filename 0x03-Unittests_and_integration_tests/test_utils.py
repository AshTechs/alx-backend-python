#!/usr/bin/env python3
"""
Unit tests for memoize decorator.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    Unit tests for memoize decorator.
    """

    class TestClass:
        def a_method(self):
            """
            A simple method that returns a constant value.
            """
            return 42

        @memoize
        def a_property(self):
            """
            A property that calls a_method, decorated with memoize.
            """
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test that a_property calls a_method once and caches the result.
        """
        test_instance = self.TestClass()

        # Setup the mock to return 42
        mock_a_method.return_value = 42

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
