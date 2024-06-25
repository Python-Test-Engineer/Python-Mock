Based on https://www.youtube.com/playlist?list=PLe4mIUXfbIqaXv8kRvUqgrMREq-p5GgdV


We are using mocking and the joke files have been split as such to show where we need to reference the 'get_joke' from.

We are testing lne(get_joke()) not get_joke() (yet!)

It needs to reference the module where it is CALLED not DEFINED.

This ties in with the lecture on monkeypatching where monkeypatch changes the sys.modules entries etc...

Hence we use @patch("joke.get_joke") and not @patch("api_joke.get_joke") as get_joke is called in joke.py not api_joke.py where it is defined:


def len_joke() -> int:
    """get length"""
    the_joke = get_joke() # called in joke.py
    return len(the_joke)