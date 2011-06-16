#!/usr/bin/env python

"""Python wrapper for the USA Spending Federal Assistance API."""

import re

from government_api import GovernmentAPI
from readable_keywords import category_args


state_codes = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
}


class Assistance(GovernmentAPI):
    """Python wrapper for the USA Spending Federal Assistance API."""

    def __init__(self):
        super(Assistance, self).__init__()
        self.state_codes = state_codes
        self._category_args = category_args

    def search(self, detail='b', **kwds):
        """Search the USA Spending Federal Contracts API."""
        kwds.update({'detail': detail})
        kwds = self._correct_keywords(**kwds)
        return self._assistance_keywords(**kwds)

    def _assistance_keywords(self, **kwds):
        """Internal method to resolve Federal Contract specific keywords."""
        for key in kwds:
            if key == 'state':
                # Change `state` keyword to FIPS parameter.
                state_abbrev = kwds.pop('state')
                fips_code = self.state_codes[state_abbrev]
                kwds['recipient_state_code'] = fips_code
            elif key == 'recip_cat_type':
                data = kwds[key]
                formatted_value = self._category_args[data]
                kwds[key] = formatted_value
        return self.call_api('faads/faads.php', **kwds)
