# Make sure you have requests installed.
# If not, you can install with `pip3 install requests`
# or `pip install requests`.
import requests


def ping(url):
    res = requests.get(url)
    return res.status_code == 200


print(ping("https://google.com"))
