#!/usr/bin/env python3
"""
This module contains a test case for the memoize decorator.
"""

import unittest
from unittest.mock import patch
from typing import Callable, Any, Dict, Tuple


def memoize(func: Callable) -> Callable:
    """
    Memoize decorator to cache the result of a method call.

    Args:
        func (Callable): The function to memoize.

    Returns:
        Callable: The memoized function.
    """
    cache: Dict[Tuple[Any, ...], Any] = {}

    def memoized_func(*args: Any) -> Any:
        """
        The memoized function.

        Args:
            *args (Any): Arguments to the function.

        Returns:
            Any: The cached result of the function call.
        """
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

        Returns:
            int: The constant value 42.
        """
        return 42

    @memoize
    def a_property(self) -> int:
        """
        Returns the result of a_method, memoized.

        Returns:
            int: The result of a_method, which is memoized.
        """
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.
    """

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method: unittest.mock.Mock) -> None:
        """
        Test a_property returns the correct result and a_method is called once.

        Args:
            mock_a_method (unittest.mock.Mock): Mock object for a_method.
        """
        test_instance = TestClass()
        self.assertEqual(test_instance.a_property(), 42)
        self.assertEqual(test_instance.a_property(), 42)
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
