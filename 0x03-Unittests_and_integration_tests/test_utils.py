#!/usr/bin/env python3
"""
Unit tests for access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with various inputs.
        
        Parameters:
        nested_map (Mapping): A dictionary-like object containing nested maps.
        path (Tuple): A tuple of keys representing the path to follow in the nested map.
        expected (Any): The expected result at the end of the path in the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map function to ensure KeyError is raised for invalid paths.
        
        Parameters:
        nested_map (Mapping): A dictionary-like object containing nested maps.
        path (Tuple): A tuple of keys representing the path to follow in the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


if __name__ == '__main__':
    unittest.main()
