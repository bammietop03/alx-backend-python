#!/usr/bin/env python3
""" A TestAccessNestedMap class that inherits from unittest.TestCase
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """
        Test for access_nested_map function in utils.py
        """
        with self.assertRaises(result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test the get_json function in utils"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test the get_json function in utils"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return the mock response
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert that requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
