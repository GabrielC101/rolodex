"""Used to define the contents of fixed length lists."""

__all__ = ['SchemaCollection', 'SchemaBase']


from collections import UserList
from typing import Callable, List, Type

from rolodex.list_schemas.fields import Field


class SchemaCollection(UserList):
    """Wrapper around a list of Schemas, providing extra functionality."""

    def get_schema(self, tokenized_list: List[str]):
        """
        Returns the first schema for which a given list is valid.
        :param tokenized_list:
        :return: Schema or None
        """
        for _schema in self:
            if _schema.is_valid(tokenized_list):
                return _schema
        return None


class SchemaBase:
    """Base class of schema used to define fixed length lists."""

    fields: List[Type[Field]] = None
    """Contains list of schema instances."""

    @property
    def validators(self) -> List[Callable]:
        """List of field validators."""
        return [_.validator for _ in self.fields]

    @property
    def descriptions(self) -> List[str]:
        """List of field descriptions."""
        return [_.description for _ in self.fields]

    def is_valid(self, list_of_values) -> bool:
        """
        Determines if a list of values is valid.

        :param list_of_values:
        :return:
        """
        if len(list_of_values) != 5:
            return False
        for i, validator in enumerate(self.validators):
            _is_valid = validator(list_of_values[i])
            if not _is_valid:
                return False
        return True

    def expected_location(self, name: str) -> int:
        """
        Returns the index location of a given field by name.

        :param name: field name.
        :return: index location of field.
        """
        for i, _ in enumerate(self.descriptions):
            if _ == name:
                return i
        raise ValueError("No expected location.")

    @property
    def length(self) -> int:
        """Length of the schema."""
        return len([_ for _ in self.fields])
