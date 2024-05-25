#!/usr/bin/env python3
'''module testing GithubOrgClient class
'''
from parameterized import parameterized, parameterized_class   # type: ignore
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from typing import Mapping, Sequence
from fixtures import TEST_PAYLOAD
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    '''unittest class
    '''
    @parameterized.expand(['google', 'abc'])
    @patch('requests.get')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        '''tests org function
        '''
        mock_response = Mock()
        mock_response.json.return_value = {'payload': 'data'}
        mock_get_json.return_value = mock_response
        instance = GithubOrgClient(org_name)
        r_value = instance.org
        self.assertEqual(r_value, {'payload': 'data'})
        mock_get_json.called_once_with(org_name)

    def test_public_repos_url(self) -> None:
        '''tests _public_repos_url function
        '''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = {'repos_url': {'some': 'data'}}
            instance = GithubOrgClient('my_Org')
            r_value = instance._public_repos_url
            self.assertEqual(r_value, {'some': 'data'})

    @patch('requests.get')
    def test_public_repos(self, mock_get_json: Mock):
        '''tests public_repos method
        '''
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub_repo:
            mock_pub_repo.return_value = 'some url'
            mock_get_requests = Mock()
            mock_get_requests.json.return_value = [{'name': 'repo1'},
                                                   {'name': 'repo2'}]
            mock_get_json.return_value = mock_get_requests
            instance = GithubOrgClient('my_Org')
            r_value = instance.public_repos()
            self.assertEqual(r_value, ['repo1', 'repo2'])
            mock_pub_repo.called_once()
            mock_get_json.called_once()

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
    def test_has_license(self,
                         repo: dict,
                         license_key: str,
                         expected_value: bool) -> None:
        '''tests has_license method
        '''
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_value)


@parameterized_class(('org_payload',
                      'repos_payload',
                      'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''tests the GithubOrgClient.public_repos method in an integration test
    by mocks code that sends external requests.
    '''

    @classmethod
    @patch('requests.get')
    def setUpClass(cls, mock_get: Mock):
        cls.get_patcher = patch('requests.get')
        cls.mock_response = cls.get_patcher.start()

        def side_effect():
            mock_gets = Mock()
            mock_gets.json.return_value = cls.repos_payload
            return mock_gets
        cls.mock_response.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    @patch('client.GithubOrgClient.repos_payload')
    def test_public_repos(self, mock_repos_payload: Mock):
        mock_repos_payload.json.return_value = TEST_PAYLOAD[0][1]
        instance = GithubOrgClient('my_Org')
        r_value = instance.public_repos()
        # self.assertEqual(r_value, TEST_PAYLOAD[0][2])
        self.assertEqual(r_value, [])

    @patch('client.GithubOrgClient.repos_payload')
    def test_public_repos_with_license(self, mock_repos_payload: Mock):
        mock_repos_payload.return_value = TEST_PAYLOAD[0][1]
        instance = GithubOrgClient('my_Org')
        r_value = instance.public_repos(license="apache-2.0")
        self.assertEqual(r_value, [])
