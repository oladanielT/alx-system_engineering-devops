#!/usr/bin/python3
"""
function to return request from a reddit Api
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit
    """
    if not subreddit:
        return
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditAPI/0.0.1"}
    params = {'limit': 10}
    try:
        response = requests.get(apiUrl, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    print(post['data']['title'])
            return (None)
    except requests.exceptions.RequestException:
        return (None)
