__all__ = ['is_name_or_color', 'is_phone_number', 'is_zip_code']


def is_name_or_color(val: str) -> bool:
    """
    Tests whether is a color or name.

    :param val:
    :return: True or False
    """
    contains_alpha = False
    contains_number = False
    if isinstance(val, str):
        for _ in val:
            if _.isalpha():
                contains_alpha = True
        for _ in val:
            if _.isnumeric():
                contains_number = True
    if contains_alpha and not contains_number:
        return True
    return False


def is_phone_number(val: str) -> bool:
    """
    Check whether string is a valid phone number.

    :param val:
    :return: True or False
    """
    digits = ''.join([_ for _ in list(val) if _.isdigit()])
    if len(digits) == 10:
        return True
    return False


def is_zip_code(val: str) -> bool:
    """
    Checks whether string is a valid zip code.

    :param val:
    :return: True or False
    """
    digits = ''.join([_ for _ in list(val) if _.isdigit()])
    if len(digits) == 5:
        return True
    return False
