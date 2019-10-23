import pytest
import data_field_cleanup as dfc

def test_business_field_import_all_capitals():
    input = 'MT ALBERT PHARMACY'
    expected = 'Mt Albert Pharmacy'
    actual = dfc.titlize_field(input)
    assert actual == expected

def test_business_field_import_with_full_stops():
    input = 'p.p.p pet product providers'
    expected = 'P.P.P Pet Product Providers'
    actual = dfc.titlize_field(input)
    assert actual == expected

def test_title_field_import_trim_full_stop():
    input = 'Mr.'
    expected = 'Mr'
    actual = dfc.trim_field(input)
    assert actual == expected

def test_dob_field_import_mmddyyyy():
    input = '03/21/1951'
    expected = '21/03/1951'
    actual = dfc.format_date_field(input)
    assert actual == expected

def test_dob_field_import_mddyyyy():
    input = '3/21/1951'
    expected = '21/03/1951'
    actual = dfc.format_date_field(input)
    assert actual == expected

def test_dob_field_import_mmdyyyy():
    input = '03/1/1951'
    expected = '01/03/1951'
    actual = dfc.format_date_field(input)
    assert actual == expected

def test_dob_field_import_mdyyyy():
    input = '3/1/1951'
    expected = '01/03/1951'
    actual = dfc.format_date_field(input)
    assert actual == expected

def test_dob_field_import_mdyy():
    input = '3/1/51'
    expected = '01/03/1951'
    actual = dfc.format_date_field(input)
    assert actual == expected

def test_dob_field_import_invalid_month():
    input = '123/1/51'
    
    with pytest.raises(Exception):
        dfc.format_date_field(input)
    
def test_dob_field_import_invalid_day():
    input = '12/44/51'
    
    with pytest.raises(Exception):
        dfc.format_date_field(input)
    
def test_number_field_valid_string_all_nums():
    input = "12345"
    expected = "12345"
    actual = dfc.format_number_field(input)
    assert actual == expected

def test_number_field_valid_string_some_nums():
    input = "12-3 4.5"
    expected = "12345"
    actual = dfc.format_number_field(input)
    assert actual == expected

def test_mobile_field_no_leading_code():
    input = "12345"
    expected = "6412345"
    actual = dfc.format_mobile_field(input)
    assert actual == expected

def test_mobile_field_has_leading_code():
    input = "6412345"
    expected = "6412345"
    actual = dfc.format_mobile_field(input)
    assert actual == expected
