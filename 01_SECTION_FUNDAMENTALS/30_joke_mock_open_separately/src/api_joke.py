"""Get joke request"""

import requests
from rich.console import Console

console = Console()



# This is where get_joke() is defined
def get_joke() :
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
