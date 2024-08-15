#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If the subreddit does not exist, return 0.
    """
    headers = {"User-Agent": "Mozilla/3.0.0/10"}
    sub_url = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit),
                           headers=headers, allow_redirects=False)
    sub = sub_url.json()
    if sub_url.status_code != 200:
        return 0
    return sub.get('data').get('subscribers')
