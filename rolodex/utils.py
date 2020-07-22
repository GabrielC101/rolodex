"""Utilities that are likely to be reused."""

__all__ = ['get_only_digits', 'format_phone_number', 'name_sort_key']


def get_only_digits(string_of_chars: str) -> str:
    """
    Given a string, return a string containing only digits.
    :param string_of_chars:
    :return: A string containing only digits (or empty).
    """
    try:
        return ''.join([_ for _ in string_of_chars if _.isdigit()])
    except AttributeError:
        raise ValueError(f'Can only get digits from string. {string_of_chars} is type {type(string_of_chars)}.')


def format_phone_number(inital_phone_number: str) -> str:
    phone_number: str = get_only_digits(inital_phone_number)
    if len(phone_number) == 10:
        return f'{phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:10]}'
    if len(phone_number) == 11 and str(phone_number[0]) == '1':
        return f'{phone_number[0]}-{phone_number[1:4]}-{phone_number[4:7]}-{phone_number[7:11]}'
    raise ValueError(f'Not a valid standard US phone number: {inital_phone_number}')


def name_sort_key(item):
    """
    Returns lastname + firstname. Used to sort dicts by lastname/firstname.

    :param item:
    :return: last name appended to first name.
    """
    return item.get('lastname', '') + item.get('firstname', '')