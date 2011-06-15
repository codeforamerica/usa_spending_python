#!/usr/bin/env python

"""Python API for the USA Spending Federal Contracts API."""

import re

from api import API
from readable_keywords import (keywords, detail_args,
                               competition_args, sort_by_args)


class Contracts(API):
    """Python wrapper for USA Spending's Federal Contracts API."""

    def __init__(self):
        super(Contracts, self).__init__()
        self.base_url = 'http://usaspending.gov'
        self.output_format = 'xml'
        self.required_params = None
        self.keywords = keywords
        self._detail_args = detail_args
        self._competition_args = competition_args
        self._sort_by_args = sort_by_args
        self._re_competition = re.compile('extent_comp.+|compet.+')
        self._re_sort_by = re.compile('sort.+')

    def search(self, detail='b', **kwargs):
        """Search the USA Spending Federal Contracts API."""
        return self._correct_keywords(detail=detail, **kwargs)

    def _correct_keywords(self, **kwargs):
        """
        Internal method to resolve human readable keywords into keywords
        used with the Federal Contracts API.
        """
        if kwargs['detail'] in self._detail_args:
            data = kwargs.pop('detail')
            kwargs['detail'] = self._detail_args[data]
        for key in kwargs:
            if self._re_competition.match(key):
                data = kwargs.pop(key)
                kwargs['extent_compete'] = self._competition_args[data]
            elif self._re_sort_by.match(key):
                data = kwargs.pop(key)
                kwargs['sortby'] = self._sort_by_args[data]
            elif key in self.keywords:
                # We need to go from human readable to the
                # correct search_type parameter name.
                correct_name = self.keywords[key]
                data = kwargs.pop(key)
                kwargs.update({correct_name: data})
        return self.call_api('fpds/fpds.php', **kwargs)
