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
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """
        Test that a_property calls a_method once and caches the result.
        """
        test_instance = self.TestClass()

        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
