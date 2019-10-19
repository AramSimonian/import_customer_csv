import data_field_cleanup as dfc

def test_business_field_import_1():
    input = 'MT ALBERT PHARMACY'
    expected = 'Mt Albert Pharmacy'
    actual = dfc.titlize_field(input)
    assert actual == expected

def test_business_field_import_2():
    input = 'p.p.p pet product providers'
    expected = 'P.P.P Pet Product Providers'
    actual = dfc.titlize_field(input)
    assert actual == expected

def test_title_field_import():
    input = 'Mr.'
    expected = 'Mr'
    actual = dfc.trim_field(input)
    assert actual == expected

def test_dob_field_import():
    input = '3/21/1951'
    expected = '21/03/1951'
    actual = dfc.format_date_field(input)
    assert actual == expected
