"""RandomUser"""

from api_random_user import get_random_user

# from pyboxen import boxen
from rich.console import Console

console = Console()


def len_email() -> int:
    """get length"""
    the_email = get_random_user()
    console.print("\n\t[blue]called [/] get_random_user() [blue]in random_user.py[/]")
    return len(the_email)
