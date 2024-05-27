"""Test joke"""

import unittest
from unittest.mock import MagicMock, patch

import pytest

from api_joke import get_joke
from joke import len_joke


class TestJoke(unittest.TestCase):
    """Test joke"""

    @pytest.mark.joke_mocks
    @patch("joke.get_joke")  # we are testing len(joke()) not api_joke.get_joke()
    def test_len_joke(self, mock_get_joke) -> None:
        """get len test"""
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    # requests has a 'shape':
    #   request.get
    #   request.get() === request.get.return_value
    #   request.status_code
    #   request.json() === request.json.return_value
    # we will need to create a mock that has this shape...

    @pytest.mark.joke_mocks
    @patch("api_joke.requests")
    def test_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        # self.assertEqual(get_joke(), {"joke": "Hello World"})
        assert get_joke() == {"joke": "Hello World"}
        assert mock_response.status_code == 200

    @pytest.mark.joke_mocks
    @patch("api_joke.requests")
    def test_fail_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        # mock_response = = MagicMock({status_code: 403}) check?
        mock_response.status_code = 403
        # this is equivalent to mock_response.json()
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        # this is equivalent to mock_response.get()
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "NO_JOKE")
        # self.assertEqual(mock_response.status_code , 200)
