#!/usr/bin/python3
""" Get the first 10 hot posts for a given subreddit """

import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit """
    subreddit_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                                  .format(subreddit),
                                  headers={"User-agent": "My-User-Agent"},
                                  allow_redirects=False)
    if subreddit_info.status_code >= 300:
        print("None")
    else:
        [print(top.get("data").get("title"))
         for top in subreddit_info.json().get("data").get("children")]
