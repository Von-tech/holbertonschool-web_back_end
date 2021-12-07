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
        {"google"),
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
