"""Joke"""

from pyboxen import boxen
from rich.console import Console

console = Console()
from .api_joke import get_joke


def len_joke() -> int:
    """get length"""
    # This is where get_joke() is called
    the_joke = get_joke()
    print("in joke.py")
    return len(the_joke)
