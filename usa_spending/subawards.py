#!/usr/bin/env python

"""Python wrapper for the USA Spending Federal Assistance API."""

import re

from government_api import GovernmentAPI


class Subawards(GovernmentAPI):
    """Python wrapper for the USA Spending Federal Assistance API."""

    def __init__(self):
        super(Subawards, self).__init__()

    def search(self, detail='b', **kwds):
        """Search the USA Spending Federal Contracts API."""
        kwds.update({'detail': detail})
        kwds = self._correct_keywords(**kwds)
        return self._assistance_keywords(**kwds)

    def _assistance_keywords(self, **kwds):
        """Internal method to resolve Federal Contract specific keywords."""
        for key in kwds:
            if key == 'state':
                state_abbrev = kwds.pop('state')
                kwds['subawardee_state_code'] = state_abbrev
        return self.call_api('fsrs/fsrs.php', **kwds)
