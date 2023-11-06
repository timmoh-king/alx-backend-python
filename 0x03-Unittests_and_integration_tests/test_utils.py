#!/usr/bin/env python3

"""
    In this task you will write the first unit test for utils.access_nested_map
    Create a TestAccessNestedMap class that inherits from unittest.TestCase
    Decorate the method with @parameterized.expand to test the function
"""

import unittest
from unittest.mock import patch, Mock
from typing import Tuple, Union, Dict
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json
)


class TestAccessNestedMap(unittest.TestCase):
    """Implement the TestAccessNestedMap.test_access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b" : 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map` function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])

    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception
            ) -> None:
        """
            Use the assertRaises context manager to test that a KeyError raised
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Define the TestGetJson(unittest.TestCase) class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    @patch('request.get')

    def test_get_json(
            self,
            url: str,
            test_payload: Dict
            ) -> None:
        """
             test that utils.get_json returns the expected result
             We don’t want to make any actual external HTTP calls
             Use unittest.mock.patch to patch requests.get
        """
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
