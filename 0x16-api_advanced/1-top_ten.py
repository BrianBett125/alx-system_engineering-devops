#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    A method that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the
    given subreddit
    Return None If not a valid subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")

    [print(child.get("data").get("title"))
        for child in results.get("children")]
