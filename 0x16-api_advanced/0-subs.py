#!/usr/bin/python3
"""
Checking number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    headers = {"User-Agent": "kali/2.0.0.1"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code < 300:
        return response.json().get("data").get("subscribers")
    return 0
