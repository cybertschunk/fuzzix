# -*- coding: utf-8 -*-
"""crawls the google search engine"""

from fuzzix.api.net.web_hooks import SearchEngine, SearchResult


class _GOOGLEAPI(SearchEngine):
    """querying the google search engine"""

    REST_API_URL = "GET https://www.googleapis.com/customsearch/v1" + \
    "?key=[API_KEY]&cx=017576662512468239146:omuauf_lfve&q=[query]"

    def __init__(self, google_api_key):
        self.google_api_key = google_api_key
        super(_GOOGLEAPI, self).__init__("Google")

    def search(self, searchstr, use_api_key_if_provided=True):
        """
        searches after a given string in the google search engine.
        Uses the rest api if an api key is provided. Otherwise it tries to
        use the normal search app
        return: A list of search results as SearchResult-objects
        """
