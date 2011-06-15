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
    ... c.search(state='NY', competition='NA')


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
