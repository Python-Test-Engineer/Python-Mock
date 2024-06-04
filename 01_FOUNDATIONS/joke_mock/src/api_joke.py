"""Get joke request"""

import requests
from pyboxen import boxen
from rich.console import Console

console = Console()


def get_joke() -> str:
    """get a joke"""
    # this is where get_joke() is defined

    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        joke = response.json()["value"]
    else:
        joke = "NO_JOKE"
    print("in api_joke.py")
    return joke


# print(len_joke())
