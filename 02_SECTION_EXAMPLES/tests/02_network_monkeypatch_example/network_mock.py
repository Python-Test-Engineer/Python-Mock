"""API"""

import requests


def get_url(url, timeout):
    """Get API"""

    return requests.get(url, timeout=timeout)
