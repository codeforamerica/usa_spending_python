#!/usr/bin/env python

"""Unit tests for the `Contracts` class in the `usa_spending` module."""

import unittest

from mock import Mock

from usa_spending import Contracts
from usa_spending.api import api


class TestContractsInit(unittest.TestCase):

    def test_default_Contracts_init(self):
        contracts = Contracts()
        self.assertEquals(contracts.base_url, 'http://usaspending.gov')
        self.assertEquals(contracts.output_format, 'xml')


class TestSearchMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_simple_search_method_query(self):
        Contracts().search(state='AL')
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'state=AL&detail=b')
        api.urlopen.assert_called_with(expected_url)

    def test_search_keyword_changes_to_correct_param(self):
        Contracts().search(zipcode=12345)
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'ZIPCode=12345&detail=b')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_changes_detail_keyword(self):
        Contracts().search(zipcode=12345, detail='complete')
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'ZIPCode=12345&detail=c')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_changes_multiple_keywords(self):
        Contracts().search(state='CA', detail='summary',
                           first_year=2009, last_year=2010)
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'first_year_range=2009&state=CA'
                        '&last_year_range=2010&detail=s')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_changes_multiple_arguments(self):
        Contracts().search(state='TX', detail='summary', competition='NA')
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'extent_compete=B&state=TX&detail=s')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_count_keyword(self):
        Contracts().search(state='NY', count=500)
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'state=NY&max_records=500&detail=b')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_changes_sort_by_keyword(self):
        Contracts().search(state='TX', sort_by='date')
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'state=TX&detail=b&sortby=d')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_expands_keyword(self):
        Contracts().search(pop_zc=12345)
        expected_url = ('http://usaspending.gov/fpds/fpds.php?'
                        'placeOfPerformanceZIPCode=12345&detail=b')
        api.urlopen.assert_called_with(expected_url)


if __name__ == '__main__':
    unittest.main()
