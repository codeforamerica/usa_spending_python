#!/usr/bin/env python

"""Python API for the USA Spending Federal Contracts API."""

import re

from government_api import GovernmentAPI
from readable_keywords import competition_args


class Contracts(GovernmentAPI):
    """Python wrapper for USA Spending's Federal Contracts API."""

    def __init__(self):
        super(Contracts, self).__init__()
        self._competition_args = competition_args
        self._re_competition = re.compile('extent_comp.+|compet.+')

    def search(self, detail='b', **kwds):
        """Search the USA Spending Federal Contracts API."""
        kwds.update({'detail': detail})
        kwds = self._correct_keywords(**kwds)
        return self._contract_keywords(**kwds)

    def _contract_keywords(self, **kwds):
        """Internal method to resolve Federal Contract specific keywords."""
        for key in kwds:
            if self._re_competition.match(key):
                data = kwds.pop(key)
                formatted_value = self._competition_args[data].upper()
                kwds['extent_compete'] = formatted_value
        return self.call_api('fpds/fpds.php', **kwds)
