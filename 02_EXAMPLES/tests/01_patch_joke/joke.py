"""Joke"""


from api_joke import get_joke


def len_joke() -> int:
    """get length"""
    the_joke = get_joke()
    print("in joke.py")
    return len(the_joke)
