from rolodex.stucts import TokenizedLine, TokenizedLineCollection

import pytest

GOOD_LINES = [
    'Annalee, Loftis, 97296, 905 329 2054, blue',
    'Liptak, Quinton, (653)-889-7235, yellow, 70703'
]

BAD_LINES = [
    'Noah, Moench, 123123121, 232 695 2394, yellow',
    'Ria Tillotson, aqua marine, 97671, 196 910 5548',
    'James Johnston, gray, 38410, 628 102 3672',
    '0.547777482345',
    'George Won, aqua marine, 97148, 488 084 5794',
    'McGrath, Luke, (555)-11111-11111111, gray, 70646'
]


@pytest.mark.parametrize('line', GOOD_LINES)
def test_tokenized_good_lines(line):
    tokenized_line = TokenizedLine(line.split(', '))
    assert tokenized_line.schema
    assert tokenized_line.is_valid
    assert tokenized_line.as_dict()
    assert tokenized_line.color
    assert tokenized_line.firstname
    assert tokenized_line.zipcode
    assert tokenized_line.lastname
    assert tokenized_line.phonenumber


@pytest.mark.parametrize('line', BAD_LINES)
def test_tokenized_bad_lines(line):
    tokenized_line = TokenizedLine(line.split(', '))
    assert not tokenized_line.schema
    assert not tokenized_line.is_valid
    assert not tokenized_line.as_dict()
    assert not tokenized_line.color
    assert not tokenized_line.firstname
    assert not tokenized_line.zipcode
    assert not tokenized_line.lastname
    assert not tokenized_line.phonenumber


def test_tokenized_line_collection():
    good_collection = TokenizedLineCollection([TokenizedLine(_.split(', ')) for _ in GOOD_LINES])
    assert good_collection.valid_dicts
    assert not good_collection.error_indexes
    assert not good_collection.all_invalid
    assert len(good_collection.error_indexes) == len(good_collection.all_invalid)
    assert not good_collection.all_invalid

    bad_collection = TokenizedLineCollection([TokenizedLine(_.split(', ')) for _ in BAD_LINES])
    assert not bad_collection.valid_dicts
    assert bad_collection.error_indexes
    assert bad_collection.all_invalid
    assert len(bad_collection.error_indexes) == len(bad_collection.all_invalid)
    assert not bad_collection.all_valid
