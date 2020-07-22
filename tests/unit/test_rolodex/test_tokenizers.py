from rolodex.tokenizers import LineTokenizer

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


def test_tokenizer():
    lines = LineTokenizer(GOOD_LINES)
    assert lines.tokenize_lines().valid_dicts
    bad_lines = LineTokenizer(BAD_LINES)
    assert not bad_lines.tokenize_lines().valid_dicts
