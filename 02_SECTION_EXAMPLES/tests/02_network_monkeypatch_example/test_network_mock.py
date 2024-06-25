"""Network Test using PyTest Monkeypatch"""

from rich.console import Console

console = Console()
from unittest.mock import MagicMock, Mock

from network_mock import get_url

console.print(globals())


def test_api_calls_gets_result(monkeypatch):
    """Test"""
    mock_result = MagicMock()  # Mock works too
    mock_result.text = "Hello World"
    mock_result.timout = 10
    mock_get = MagicMock(return_value=mock_result)  # Mock works too
    monkeypatch.setattr("requests.get", mock_get)
    result = get_url("https://randomuser.me/api/", timeout=10)  # see globals() output
    mock_get.assert_called_once_with("https://randomuser.me/api/", timeout=10)
    assert result.text == "Hello World"
