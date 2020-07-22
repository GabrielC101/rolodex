__all__ = ['sort']


def sort(*decorator_args, **decorator_kwargs):  # pylint: disable=unused-argument
    key = decorator_kwargs.get('key', None)
    reverse = decorator_kwargs.get('reverse', False)

    def wrapper(func):

        def wrapped(*function_args, **function_kwargs):
            result = func(*function_args, **function_kwargs)
            if isinstance(result, dict):
                result = dict(sorted(result.items(), key=key, reverse=reverse))
            if isinstance(result, list):
                result = sorted(result, key=key, reverse=reverse)
            return result

        return wrapped

    return wrapper
