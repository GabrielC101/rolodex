from rolodex.validators import is_name_or_color, is_phone_number, is_zip_code

import pytest

VALID_NAME_OR_COLOR = [
    'Green',
    'green',
    'Mr. Gabriel',
    'Mary Sue',
    'aqua marine',
    'foo',
    'a',
    'haberdashery'
]

INVALID_NAME_OR_COLOR = [
    'Gre3n',
    '',

]

VALID_PHONE_NUMBER = [
    '1234567890',
    '(222) 222-2222',
    'T 800 333 2222',
    'FIN (800) THE (222) DUDE (3456)'
]


INVALID_PHONE_NUMBER = [
    '123a567890',
    '(22) 222-2222',
    '18003332222',
    'FIN (800) THE (222) DUDE (456)'
]

VALID_ZIP_CODES = [
    '23456',
    '42645',
    '84932',
    '23042',
]

INVALID_ZIP_CODES = [
    '23456-2223',
    '123',
    'aaaaa',
    ''
]


@pytest.mark.parametrize('name_or_color', VALID_NAME_OR_COLOR)
def test_is_name_or_color_true(name_or_color):
    assert is_name_or_color(name_or_color)


@pytest.mark.parametrize('name_or_color', INVALID_NAME_OR_COLOR)
def test_is_name_or_color_false(name_or_color):
    assert not is_name_or_color(name_or_color)


@pytest.mark.parametrize('phonenumber', VALID_PHONE_NUMBER)
def test_is_phonenumber_true(phonenumber):
    assert is_phone_number(phonenumber)


@pytest.mark.parametrize('phonenumber', INVALID_PHONE_NUMBER)
def test_is_phonenumber_false(phonenumber):
    assert not is_phone_number(phonenumber)


@pytest.mark.parametrize('zipcode', VALID_ZIP_CODES)
def test_is_zip_code(zipcode):
    assert is_zip_code(zipcode)


@pytest.mark.parametrize('zipcode', INVALID_ZIP_CODES)
def test_is_zip_code_false(zipcode):
    assert not is_zip_code(zipcode)
