"""Test joke"""

import unittest
from unittest.mock import MagicMock, patch

import pytest
from pyboxen import boxen
from rich.console import Console

console = Console()
from src.api_joke import get_joke
from src.joke import len_joke


class TestJoke(unittest.TestCase):
    """Test joke"""

    def test_0100_no_patch(self):
        """no patch"""
        joke = get_joke()
        console.print("\n->[yellow]0100 not patched[/]", joke)
        self.assertEqual(3, 3)

    @patch("src.joke.get_joke")
    def test_0200_len_joke(self, mock_get_joke) -> None:
        """get len test"""
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    @patch("src.api_joke.requests")
    def test_0300_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        # self.assertEqual(get_joke(), {"joke": "Hello World"})
        assert get_joke() == {"joke": "Hello World"}
        assert mock_response.status_code == 200

    @patch("src.api_joke.requests")
    def test_0400_fail_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "NO_JOKE")
        # self.assertEqual(mock_response.status_code , 200)
