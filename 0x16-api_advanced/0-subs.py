#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    return the number of subscribers.
    """
    if subreddit:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if data or 'data' in data or 'subscribers' and data['data']:
            return data['data']['subscribers']
    return 0
