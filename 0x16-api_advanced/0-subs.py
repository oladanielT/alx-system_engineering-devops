#!/usr/bin/python3
"""
Getting the number of reddit sub
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    headers = {"User-Agent": "best-agent"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code >= 300:
        return 0
    return res.json().get("data").get("subscribers")
