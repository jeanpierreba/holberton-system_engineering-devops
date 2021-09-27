#!/usr/bin/python3
""" Find the number of subscribers of a subreddit """

import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers """
    subreddit_info = requests.get("https://www.reddit.com/r/{}/about.json"
                                  .format(subreddit),
                                  headers={"User-agent": "My-User-Agent"},
                                  allow_redirects=False)
    if subreddit_info.status_code >= 300:
        return 0
    return subreddit_info.json().get("data").get("subscribers")
