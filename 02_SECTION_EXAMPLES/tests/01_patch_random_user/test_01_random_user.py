"""Test joke"""

import unittest
from unittest.mock import MagicMock, patch
from rich.console import Console


from api_random_user import get_random_user  # don't need this in mcok but used for demo
from random_user import len_email

console = Console()


class TestEmail(unittest.TestCase):
    """Test joke"""

    # we are testing len(email()) not api_random_user.get_email()
    @patch("random_user.get_random_user")
    def test_01_len_email(self, mock_get_email) -> None:
        """get len test"""
        mock_get_email.return_value = "alan@example.com"  # 16 chars
        # if we were using actual api call
        email = get_random_user()
        console.print(f"[blue]email from api: {email['results'][0]['email']}[/]")

        self.assertEqual(len_email(), 16)

    # requests has a 'shape':
    #   request.get
    #   request.get() === request.get.return_value
    #   request.status_code
    #   request.json() === request.json.return_value
    # we will need to create a mock that has this shape...
    @patch("api_random_user.requests")
    def test_02_get_random_user(self, mock_requests):
        """mocking requests"""
        # what we are sauing is api_random_user.get_random_user() is patched with our mock_response when we call get_random_user()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = "alan@example.com"
        mock_requests.get.return_value = mock_response
        # self.assertEqual(get_random_user(), {"email": "alan@example.com"})
        assert get_random_user() == "alan@example.com"
        assert mock_response.status_code == 200

    #
    @patch("api_random_user.requests")
    def test_03_fail_get_random_user(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        # mock_response = = MagicMock({status_code: 403}) check?
        mock_response.status_code = 403
        # this is equivalent to mock_response.json()
        mock_response.json.return_value = "alan@example.com"
        # this is equivalent to mock_response.get()
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_random_user(), "NONE")
        # self.assertEqual(mock_response.status_code , 200)
