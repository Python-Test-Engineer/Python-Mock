# https://dev.to/quame_jnr1/mocking-requests-in-python-2anc

import unittest
from unittest.mock import patch, Mock
from client import ping


class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "https://google.com"

    def test_ping_returns_200(self):
        result = ping(self.url)
        self.assertTrue(result)

    @patch("client.requests")  # New
    def test_ping_returns_500(self, mock_requests):  # New

        # New
        mock_response = Mock()  # article has MagicMock
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response

        result = ping(self.url)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
