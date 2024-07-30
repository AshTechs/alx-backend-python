#!/usr/bin/env python3
"""
Integration test module for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test case for GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock external requests.
        """
        cls.get_patcher = patch('requests.get')

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

        # Define the side effects for different URLs
        cls.mock_get.side_effect = cls.get_side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher.
        """
        cls.get_patcher.stop()

    @staticmethod
    def get_side_effect(url):
        """
        Side effect method for requests.get to return different fixtures
        based on the URL.
        """
        if url == "https://api.github.com/orgs/google":
            return MockResponse(org_payload)
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(repos_payload)
        return MockResponse(None)

    def test_public_repos(self):
        """
        Test public_repos method to ensure it returns the correct list of repos
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method to ensure it filters repos by license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), apache2_repos)


class MockResponse:
    """
    MockResponse class to simulate the response object returned by requests.get
    """
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


if __name__ == '__main__':
    unittest.main()
