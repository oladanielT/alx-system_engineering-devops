#!/usr/bin/python3
"""
function to return a request from reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    module to return number of subscribers if exists and 0 if not
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data["data"]["subscribers"]
            return 0
        return 0
    except requests.exceptions.RequestException:
        return 0
    