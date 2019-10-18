import data_field_cleanup as dfc

def test_business_field_import():
    input = "MT ALBERT PHARMACY"
    expected = "Mt Albert Pharmacy"
    actual = dfc.cleanup_business_field(input)
    assert actual == expected
