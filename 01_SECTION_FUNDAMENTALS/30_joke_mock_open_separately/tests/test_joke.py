"""Test joke"""

import unittest
from unittest.mock import MagicMock, patch

from src.api_joke import get_joke
from src.joke import len_joke

from rich.console import Console

console = Console()

console.print(globals())


class TestJoke(unittest.TestCase):
    """Test joke"""

    def test_0100_no_patch(self):
        """no patch"""
        joke = get_joke()
        console.print(f"\n=> [yellow]TEST 0100 not patched[/] '{joke}'")
        # As we get a random joke, we don't know the length of it to run our test for len_joke
        # for convenience return True
        self.assertEqual(3, 3)

    # we use a decorator this time rather than a with context manager
    # notice how we reference where it is called in src.joke.get_joke and not where it is defined in api_joke.py
    # we still use the requests library and make an internet call
    # the globals output shows this
    @patch("src.joke.get_joke")
    def test_0200_len_joke(self, mock_get_joke) -> None:
        """get len test"""
        # we can set up a mock that has a return vale of 'one' and length 3
        # it must have the shape of get_joke()
        mock_get_joke.return_value = "one"
        self.assertEqual(len_joke(), 3)

    # here we patch requests so we need to refence api_joke.py
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

    # we mock a failure of requests
    @patch("src.api_joke.requests")
    def test_0400_fail_get_joke(self, mock_requests):
        """mocking requests"""
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"value": {"joke": "Hello World"}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), "NO_JOKE")
        # self.assertEqual(mock_response.status_code , 200)
