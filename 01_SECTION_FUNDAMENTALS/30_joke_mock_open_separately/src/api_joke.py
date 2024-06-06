"""Get joke request"""

import requests
from pyboxen import boxen
from rich.console import Console

console = Console()


stub = {
    "categories": [],
    "created_at": "2020-01-05 13:42:21.179347",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "d0ewqdGHQKyeyMf50RooKw",
    "updated_at": "2020-01-05 13:42:21.179347",
    "url": "https://api.chucknorris.io/jokes/d0ewqdGHQKyeyMf50RooKw",
    "value": "Chuck Norris did not call the wrong number.You answered the wrong phone.",
}


def get_joke() -> str:
    """get a joke"""
    # this is where get_joke() is defined
    console.print("\n->[green]in api_joke.py.getjoke()[/]")
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        joke = response.json()["value"]
        print("\n--------- Requests Joke --------")
        console.print(
            f"=> [green]Joke from get_joke() in api_joke.py:[/] '{joke}' with length: {len(joke)}"
        )
        print("--------- Requests Joke --------")
        # joke = stub["value"] # does not work as the value changes each time
    else:
        joke = "NO_JOKE"

    return joke
