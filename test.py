#!/usr/bin/env python

"""Unit tests for the `Contracts` class in the `usa_spending` module."""

import unittest

from mock import Mock

from usa_spending import GovernmentAPI, Contracts, Assistance
from usa_spending.api import api


class TestGovernmentAPI(unittest.TestCase):

    def test_GovernmentAPI_init(self):
        gov = GovernmentAPI()
        self.assertEquals(gov.base_url, 'http://usaspending.gov')
        self.assertEquals(gov.output_format, 'xml')
        self.assertFalse(gov.api_key)
        self.assertFalse(gov.required_params)

class TestGovernmentAPICorrectKeywordsMethod(unittest.TestCase):

    def setUp(self):
        self.correct_keywords = GovernmentAPI()._correct_keywords

    def test_simple_correct_keywords_call(self):
        keys = self.correct_keywords(test='foo')
        self.assertEquals(keys, {'test': 'foo'})

    def test_correct_keywords_with_detail_keyword(self):
        keys = self.correct_keywords(detail='summary', test='foo')
        self.assertEquals(keys, {'detail': 's', 'test': 'foo'})

    def test_correct_keywords_with_sort_by_keyword(self):
        keys = self.correct_keywords(state='TX', sort_by='agency')
        self.assertEquals(keys, {'sortby': 'g', 'state': 'TX'})

    def test_correct_keywords_changes_multiple_keywords(self):
        keys = self.correct_keywords(state='CA', sort_by='contractor',
                                     first_year=2009, last_year=2010)
        expected_keys = {
            'state': 'CA', 'sortby': 'r',
            'first_year_range': 2009, 'last_year_range': 2010,
        }
        self.assertEquals(keys, expected_keys)


class TestContractsInit(unittest.TestCase):

    def test_default_Contracts_init(self):
        contracts = Contracts()
        self.assertEquals(contracts.base_url, 'http://usaspending.gov')
        self.assertEquals(contracts.output_format, 'xml')


class TestContractsSearchMethod(unittest.TestCase):

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


class TestAssistanceInit(unittest.TestCase):

    def test_Assistance_init(self):
        assistance = Assistance()
        self.assertEquals(assistance.base_url, 'http://usaspending.gov')
        self.assertEquals(assistance.output_format, 'xml')


class TestAssistanceSearchMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_simple_search_method_query(self):
        Assistance().search(state='TX')
        expected_url = ('http://usaspending.gov/faads/faads.php?'
                        'detail=b&recipient_state_code=48')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_changes_keywords(self):
        Assistance().search(state='CA', year=2008)
        expected_url = ('http://usaspending.gov/faads/faads.php?'
                        'fiscal_year=2008&recipient_state_code=06&detail=b')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_returns_regular_xml_output(self):
        Assistance().search(state='NY', count=500, output_format=None)
        expected_url = ('http://usaspending.gov/faads/faads.php?'
                        'max_records=500&recipient_state_code=36&detail=b')
        api.urlopen.assert_called_with(expected_url)
        self.assertFalse(api.xml2dict.called)

    def test_search_method_replaces_recipient_state_keyword(self):
        Assistance().search(recipient_state='TX')
        expected_url = ('http://usaspending.gov/faads/faads.php?'
                        'detail=b&recipient_state_code=48')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_replaces_recipient_category_keyword(self):
        Assistance().search(recipient_category='non-profit')
        expected_url = ('http://usaspending.gov/faads/faads.php?'
                        'detail=b&recip_cat_type=n')
        api.urlopen.assert_called_with(expected_url)


if __name__ == '__main__':
    unittest.main()
