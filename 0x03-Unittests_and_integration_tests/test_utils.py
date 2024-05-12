#!/usr/bin/env python3
""" A TestAccessNestedMap class that inherits from unittest.TestCase
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ A TestAccessNestedMap class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test for access_nested_map function in utils.py
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    def test_access_nested_map_exception(self):
        """
        Test for access_nested_map function in utils.py
        """
        nested_map = {}
        path = ("a",)
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

        nested_map = {"a": 1}
        path = ("a", "b")
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
