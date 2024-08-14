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
        try:

            response = requests.get(url, headers=headers)
            if response.status_code == 404:
                return 0
            if response.status_code == 200:
                data = response.json()
                if data or 'data' in data or 'subscribers' and data['data']:
                    return data['data']['subscribers']
        except requests.exceptions.RequestException:
            return 0
    return 0
