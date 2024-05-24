#!/usr/bin/env python3
"""module implementing parameterized
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch, NonCallableMock
from utils import memoize, access_nested_map as n_map, get_json as g_json
from typing import Union, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    '''class testing access_nested_map function
    '''
    @parameterized.expand([({"a": 1}, ("a",), 1),
                          ({"a": {"b": 2}}, ("a",), {'b': 2}),
                          ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Union[int, Mapping]) -> None:
        '''actual test conglomerating several tests to one
        '''
        self.assertEqual(n_map(nested_map, path), expected)

    @parameterized.expand([({}, 'a'),
                           ({'a': 1}, ('a', 'b'))])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        '''tests exception raising in access_nested_map function
        '''
        with self.assertRaises(KeyError):
            n_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''class testing get_json method
    '''
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self,
                      test_url: str,
                      test_payload: Mapping,
                      mock_requests_get: Mock) -> None:
        '''Mock the response
        '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        '''complete patching requests.get to get_json
        using mock_requests_get as our anchor
        '''
        mock_requests_get.return_value = mock_response
        result = g_json(test_url)
        '''Test that the mocked get method was called exactly
        once (per input) with test_url
        '''
        mock_requests_get.assert_called_once_with(test_url)
        '''Test that the output of get_json is equal to test_payload.
        '''
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''class testing memoization function
    '''
    @parameterized.expand([42, 42])
    def test_memoize(self, r_value: int) -> None:
        '''actually tests memoiozation
        '''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        @patch('TestClass.a_method')
        def test_a_memoize(self, r_value: int, mock_a_method: Mock) -> None:
            '''Use unittest.mock.patch to mock a_method.
            '''
            mock_a_method.return_value = r_value
            instance = TestClass()
            '''Test that calling a_property twice, correct result is returned
            but a_method is only called once using assert_called_once.
            This is because memoization is like caching
            '''
            result = instance.a_property()
            result2 = instance.a_property()
            self.assertEqual(result, r_value)
            mock_a_method.assert_called_once()
