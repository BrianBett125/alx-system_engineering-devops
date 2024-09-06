#!/usr/bin/python3
"""
A module that has a recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    A method that writes a recursive function that queries
    the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    Return None if no valid subreddit
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
