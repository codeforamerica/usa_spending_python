#!/usr/bin/env python

"""Generalized Python wrapper for the USA Spending API."""

import re

from api import API
from readable_keywords import keywords, detail_args, sort_by_args


class GovernmentAPI(API):
    """
    Generalized Python wrapper for the USA Spending API. Resolves keyword
    replacement and connecting with the API.
    """

    def __init__(self):
        super(GovernmentAPI, self).__init__()
        self.base_url = 'http://usaspending.gov'
        self.output_format = 'xml'
        self.required_params = None
        self.keywords = keywords
        self._detail_args = detail_args
        self._sort_by_args = sort_by_args
        self._re_sort_by = re.compile('sort.+')

    def _correct_keywords(self, **kwds):
        """
        Internal method to resolve human readable keywords into keywords
        used with the Federal Contracts API.
        """
        if 'detail' in kwds and kwds['detail'] in self._detail_args:
            data = kwds.pop('detail')
            formatted_value = self._detail_args[data]
            kwds['detail'] = formatted_value
        for key in kwds:
            if self._re_sort_by.match(key):
                data = kwds.pop(key)
                formatted_value = self._sort_by_args[data]
                kwds['sortby'] = formatted_value
            elif key in self.keywords:
                # We need to go from human readable to the
                # correct search_type parameter name.
                correct_name = self.keywords[key]
                data = kwds.pop(key)
                kwds.update({correct_name: data})
        return kwds
