#!/usr/bin/env python3
""" A TestAccessNestedMap class that inherits from unittest.TestCase
"""
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ A TestAccessNestedMap class that inherits from unittest.TestCase"""

    def test_access_nested_map(self):
        """
        Test for access_nested_map function in utils.py
        """
        nested_map = {"a": {"b": {"c": 1}}}
        result = access_nested_map(nested_map, ["a", "b", "c"])

        self.assertEqual(result, 1)
        self.assertIsInstance(result, int)

        nested_map2 = {"a": ["b", "c", "d"]}
        with self.assertRaises(KeyError):
            access_nested_map(nested_map2, ["a", "b"])

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
