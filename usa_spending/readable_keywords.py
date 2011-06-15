#!/usr/bin/env python

"""
Human readable keywords for the USA Spending API -- since parameters seem to
be either snake_case or CamelCase at random.
"""

keywords = {
    'business_indicator': 'busn_indctr',
    'contract_requirement': 'descriptionOfContractRequirement',
    'description_of_contract_requirement': 'descriptionOfContractRequirement',
    'duns': 'duns_number',
    'compete': 'extent_compete',
    'competition': 'extent_compete',
    'count': 'max_records',
    'max': 'max_records',
    'from': 'records_from',
    'start': 'records_from',
    'first_year': 'first_year_range',
    'last_year': 'last_year_range',
    'place_of_performace_congressional_district': 'pop_cd',
    'place_of_performance_zip_code': 'placeOfPerformanceZIPCode',
    'pop_z': 'placeOfPerformanceZIPCode',
    'pop_zc': 'placeOfPerformanceZIPCode',
    'place_of_performance_country_code': 'placeOfPerformanceCountryCode',
    'pop_cc': 'placeOfPerformanceCountryCode',
    'piid': 'PIID',
    'sort_by': 'sortby',
    'state_code': 'stateCode',
    'vendor_country_code': 'vendorCountryCode',
    'year': 'fiscal_year',
    'zipcode': 'ZIPCode',
    'zip_code': 'ZIPCode',
}

detail_args = {
    'basic': 'b',
    'all': 'c',
    'complete': 'c',
    'list': 'l',
    'low': 'l',
    'medium': 'm',
    'profiles': 'm',
    'summary': 's',
}

competition_args = {
    'f': 'F',
    'competed SAP': 'F',
    'g': 'G',
    'not competed SAP': 'G',
    'non-competitive delivery order': 'NDO',
    'ndo': 'NDO',
    'not competed': 'C',
    'c': 'C',
    'na': 'B',
    'NA': 'B',
    'not available': 'B',
    'not available for competition': 'B',
    'b': 'B',
    'full': 'A',
    'full and open': 'A',
    'a': 'A',
    'competitive delivery order': 'CDO',
    'cdo': 'CDO',
}

sort_by_args = {
    'contractor': 'r',
    'recipient': 'r',
    'agency': 'g',
    'product': 'p',
    'service': 'p',
    'date': 'd',
}
