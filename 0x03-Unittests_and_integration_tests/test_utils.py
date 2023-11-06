#!/usr/bin/env python3

"""
    In this task you will write the first unit test for utils.access_nested_map
    Create a TestAccessNestedMap class that inherits from unittest.TestCase
    Decorate the method with @parameterized.expand to test the function
"""

import unittest
from typing import Tuple, Union, Dict
from parameterized import parameterized
from utils import access_nested_map


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
