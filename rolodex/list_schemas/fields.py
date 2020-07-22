__all__ = ['Field']

from importlib import import_module
from typing import Callable


class Field:
    """Used to specify an item in a fixed length list."""

    def __init__(self, validator, description, required=True):
        try:
            if isinstance(validator, str):
                module_name = '.'.join(validator.split('.')[0:-1])
                validator_name = validator.split('.')[-1]
                module = import_module(module_name)
                validator = getattr(module, validator_name)
        except:
            raise ValueError(f'Validator is a string, but not the path to a function: {validator}')
        self.validator: Callable = validator
        self.description: str = description
        self.required: bool = required
