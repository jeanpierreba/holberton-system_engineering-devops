#!/usr/bin/python3
""" Module that returns a list of articles """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles of all hot articles
    for a given subreddit """
    if after is None:
        return hot_list
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    subreddit_info = requests.get(url,
                                  params={"limit": 100,
                                      "after": after},
                                  headers={"User-agent": "My-User-Agent"},
                                  allow_redirects=False)
    if subreddit_info.status_code != 200:
        return None
    list_hot = hot_list + [top.get("data").get("title")
                           for top in subreddit_info.json()
                           .get("data").get("children")]
    information = subreddit_info.json()
    if not information.get("data").get(after):
        return list_hot
    return recurse(subreddit, list_hot, after)
