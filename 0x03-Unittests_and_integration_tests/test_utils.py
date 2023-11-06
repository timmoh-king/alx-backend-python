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
    get_json,
    memoize
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
            test_url: str,
            test_payload: Dict
            ) -> None:
        """
             test that utils.get_json returns the expected result
             We don’t want to make any actual external HTTP calls
             Use unittest.mock.patch to patch requests.get
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("requests.get", return_value=mock_response):
            result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
        Create TestMemoize(unittest.TestCase) class with a test_memoize method
    """
    def test_memoize(self):
        """
            Inside test_memoize, define following class
        """
        class TestClass:
            """Example class given"""
            def a_method(self):
                """return 42"""
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_get:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
