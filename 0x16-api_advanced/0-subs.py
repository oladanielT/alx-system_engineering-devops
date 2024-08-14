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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            # Correctly check for keys in the JSON response
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        return 0
    except requests.exceptions.RequestException:
        # Return 0 if there's a request error
        return 0
