"""Get joke request"""

from time import sleep
import requests
from pyboxen import boxen
from rich.console import Console

console = Console()

SLEEP_TIME = 0.5


def get_random_user():
    """get a random user"""
    console.print("\n[red]in api_random_user.py - getting data...[/]")
    url = "https://randomuser.me/api/"

    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        user = response.json()
    else:
        user = "NONE"

    sleep(SLEEP_TIME)
    return user


if __name__ == "__main__":
    email = get_random_user()["results"][0]["email"]
    console.print(f"[green]email:[/] [blue]{email}[/]")
