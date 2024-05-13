#!/usr/bin/env python3
""" Test for classes and method in client.py
"""
import unittest
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Class to test for Method Org"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test for Method Org"""
        expected_result = {"name": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        """ Test _public_repos_url method"""
        org_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload

            client = GithubOrgClient("testorg")
            result = client._public_repos_url
            self.assertEqual(
                result, "https://api.github.com/orgs/testorg/repos")
