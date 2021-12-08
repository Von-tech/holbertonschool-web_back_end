#!/usr/bin/env python3
""" Now we will test the clients.py file """
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from requests import Response
from unittest.mock import Mock, PropertyMock, patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ New class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org_name):
        """ Test func for .org """
        with patch('client.GithubOrgClient.org') as m_org:
            client = GithubOrgClient(org_name)
            self.assertEqual(client.org.return_value, m_org.return_value)

    def test_public_repos_url(self):
        """ Another test """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)\
                as m_org:
            m_org.return_value = {"repos_url": True}
            client = GithubOrgClient("org_name")
            self.assertEqual(client._public_repos_url, True)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Method in order to unit-test GithubOrgClient.has_license """
        The_test = GithubOrgClient('org_name')
        self.assertEqual(The_test.has_license(repo, license_key), expected)
