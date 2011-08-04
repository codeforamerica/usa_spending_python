#!/usr/bin/env python
"""
Author: Zach Williams, <zach AT codeforamerica DOT org>

Copyright (c) 2011, Code for America. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary form
must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with
the distribution. Neither the name of Code for America nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission. THIS SOFTWARE IS PROVIDED
BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
USA Spending Python API
=======================

Python API for the numerous APIs available through [USA
Spending](http://usaspending.gov/data?carryfilters=on).


Usage
-----

    >>> from usa_spending import Contracts
    >>> c = Contracts()
    >>> c.search(state='TX', count=500)

    >>> # Search for contracts for a specific year.
    ... c.search(zipcode=12345, year=2010)

    >>> # Search for contracts within a date range.
    ... c.search(state='CA', first_year=2008, last_year=2010)

    >>> # Search for contracts not competed on.
    ... c.search(state='NY', competition='not competed')

    >>> # Search for contracts not available for competition.
    ... c.search(state='NY', competition='N/A')

    >>> # Find the number of contracts matching your criteria.
    ... data = c.search(zipcode=12345)
    >>> found = data.response.result.numFound
    >>> print found
    6789


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
"""

setup(name="usa_spending",
      version="1.0",
      description=("Python API for the numerous APIs available through "
                   "USA Spending."),
      long_description=long_description,
      keywords="usa_spending, USA Spending, usa api",
      author="Zach Williams",
      author_email="zach@codeforamerica.org",
      url="https://github.com/codeforamerica/usa_spending_python",
      license="BSD",
      packages=["usa_spending"],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test.py",
      tests_require=["mock", "Mock"])
