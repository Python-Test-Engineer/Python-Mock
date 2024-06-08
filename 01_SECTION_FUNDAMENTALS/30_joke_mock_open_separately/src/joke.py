"""Joke"""

from rich.console import Console
from .api_joke import get_joke

console = Console()


# This is where get_joke() is called
def len_joke() -> int:
    """get length"""
    # This is where get_joke() is called
    # patch where it is CALLED not DEFINED
    the_joke = get_joke()
    console.print("\n\t[blue]in joke.py[/]", the_joke, len(the_joke))
    return len(the_joke)
