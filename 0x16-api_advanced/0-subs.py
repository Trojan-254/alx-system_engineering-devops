#!/usr/bin/python3
"""reddit module"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers
    for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
