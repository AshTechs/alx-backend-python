#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos method."""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for different URLs
        def get_side_effect(url):
            if url == "https://api.github.com/orgs/test-org":
                return MockResponse(org_payload)
            elif url == "https://api.github.com/orgs/test-org/repos":
                return MockResponse(repos_payload)
            return MockResponse(None, 404)

        cls.mock_get.side_effect = get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method."""
        client = GithubOrgClient("test-org")
        self.assertEqual(client.public_repos(), expected_repos)


class MockResponse:
    """Mock response class for requests.get."""
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    @property
    def status_code(self):
        return self.status_code


if __name__ == "__main__":
    unittest.main()
