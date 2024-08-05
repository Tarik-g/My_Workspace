"""
google_search
============

Module to search Google via Python

Author:
    Tarik Gökmen (tarikgokmen1999@gmail.com)

Version:
    1.0.0

Date:
    2024-08-05

Functions:
    search_google(search_request): Opens Goggle with the search request
"""

import sys
import webbrowser
import urllib.parse

def search_google(search_request):
    """
    Opens Goggle with the search request

    only searches reddit, geekforgeeks, github and stackoverflow

    Parameters:
    search_request (str): search request

    Author:
        Tarik Gökmen (tarikgokmen1999@gmail.com)

    Version:
        1.0.0

    Date:
        2024-08-05
    """
    sites = [
        "github.com",
        "stackoverflow.com",
        "geeksforgeeks.org",
        "reddit.com"
        ]

    site_query = " OR ".join(f"site:{site}" for site in sites)
    full_query = f"{search_request} ({site_query})"

    encoded_query = urllib.parse.quote(full_query)

    url = f"https://www.google.com/search?q={encoded_query}"

    #open Google with the search request and only brwose the sites
    webbrowser.open(url)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_request = " ".join(sys.argv[1:])
        search_google(search_request)
    else:
        print("Please provide a search query.")