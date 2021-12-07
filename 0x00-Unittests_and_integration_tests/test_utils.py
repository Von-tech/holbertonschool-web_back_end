#!/usr/bin/env python3
""" Task 0. Parameterize a unit test """
import unittest
import requests
import json
from unittest.mock import patch
from unittest import mock, TestCase
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class that inherits from unittest.TestCase """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Method to test that KeyError is raised for the following inputs """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ New class to test get_json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_request):
        """ Method to test that utils.get_json returns the expected result """
        mock_request().json.return_value = test_payload
        mock_request.assert_called_once()
        expected = get_json(test_url)
        self.assertEqual(expected, test_payload)


class TestMemoize(unittest.TestCase):
    """ New class, testing with memoization """
    def test_memoize(self):
        """ Defining new class within this method """

        class TestClass:
            def a_method(self):
                """ Method within new class that tests with exit status 42 """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, "a_method") as mock_42:
            tmp = TestClass()
            self.assertEqual(tmp.a_property, 42)
            self.assertEqual(tmp.a_property, 42)
            mock_42.assert_called_once()
