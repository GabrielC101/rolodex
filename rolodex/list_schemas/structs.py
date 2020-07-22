__all__ = ['AbstractTokenizedLineCollection', 'AbstactTokenizedLine']


from collections import UserList
from typing import Dict, List, Optional

from rolodex.list_schemas.decorators import sort


class AbstractTokenizedLineCollection(UserList):

    @property
    def all_valid(self):
        return [_ for _ in self if _.is_valid]

    @property
    def all_invalid(self):
        return [_ for _ in self if not _.is_valid]

    @property
    def error_indexes(self):
        ret = []
        for i, _lines in enumerate(self):
            if _lines in self.all_invalid:
                ret.append(i)
        return ret


class AbstactTokenizedLine(list):
    """Abstract tokenized line. Must be implemented via subclass."""

    # Must be defined
    schemas = None

    @sort()
    def as_dict(self) -> Optional[Dict]:
        """Returns a valid tokenized line as a dict."""
        if self.is_valid:
            return {_: getattr(self, _) for _ in self.schema.descriptions}
        return None

    @property
    def is_valid(self):
        if self.schema:
            return True
        return False

    @property
    def schema(self):
        return self.schemas.get_schema(self)

    def get(self, item):
        if self.is_valid:
            return self[self.schema.expected_location(item)]
        return None

    def __getattr__(self, val):
        """Allow attribute access based on schema description."""
        return self.get(val)


class TokenizedLineCollection(AbstractTokenizedLineCollection):
    """A collection of tokenized lines."""

    @property
    def valid_dicts(self) -> List[Dict[str, str]]:
        """All valid lines converted into a list of dictionaries."""
        return [_.as_dict() for _ in self.all_valid]
