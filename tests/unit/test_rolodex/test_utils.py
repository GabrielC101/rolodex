from typing import Dict, List

from rolodex.utils import format_phone_number, get_only_digits, name_sort_key

import pytest

RESULTS = [
    ('1234a', '1234'),
    ('ABCD3', '3'),
    ('ABC', ''),
    ('', '')
]


PHONE_NUMBERS = [
    ('2222D223333', '222-222-3333'),
    ('222A2223333', '222-222-3333'),
    ('222AASD222FASD3333', '222-222-3333'),
    ('222A222V3333', '222-222-3333'),

]


@pytest.mark.parametrize('arg, result', RESULTS)
def test_get_only_digits(arg, result):
    assert result == get_only_digits(arg)


@pytest.mark.parametrize('arg, result', PHONE_NUMBERS)
def test_format_phone_numbers(arg, result):
    assert result == format_phone_number(arg)

import pytest

SORTED_DICTS_FIXTURES: List[List[Dict[str, str]]] = [
    [
        {'firstname': 'Bob', 'lastname': 'Smith', 'order': 2},
        {'firstname': 'Harry', 'lastname': 'Green', 'order': 0},
        {'firstname': 'Lucy', 'lastname': 'Greenwhich', 'order': 1}
    ],
    [
        {'firstname': 'Bob', 'lastname': 'S', 'order': 1},
        {'firstname': 'Harry', 'lastname': 'Q', 'order': 0},
        {'firstname': 'Lucy', 'lastname': 'T', 'order': 2}
    ],
    [
        {'firstname': 'C', 'lastname': 'A', 'order': 0},
        {'firstname': 'B', 'lastname': 'B', 'order': 1},
        {'firstname': 'A', 'lastname': 'C', 'order': 2}
    ]
]


@pytest.mark.parametrize("list_of_dicts", SORTED_DICTS_FIXTURES)
def test_name_sort_key_pass(list_of_dicts):
    sorted_list_of_dicts: List[Dict[str, str]] = sorted(list_of_dicts, key=name_sort_key)

    for i, item in enumerate(sorted_list_of_dicts):
        assert item['order'] == i