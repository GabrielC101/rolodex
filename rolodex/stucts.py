"""Custom data structures."""

# TokenizedLineCollection included for backwards compatibility (with pytest testing)/
__all__ = ['TokenizedLine', 'TokenizedLineCollection']

from typing import Optional

from rolodex.list_schemas.schemas import SchemaCollection
from rolodex.list_schemas.structs import AbstactTokenizedLine, TokenizedLineCollection
from rolodex.schemas import schema_collection
from rolodex.utils import format_phone_number, get_only_digits


class TokenizedLine(AbstactTokenizedLine):
    """Represents a tokenized line. Each tokenized line contains a schema collection. There are several possible schemas
    a tokenized line may correspond to. The schema attribute dynamically determines the first valid schema, which is
    considered the correct schema. The schema's description attribute is used to give each of the items in the line
    named values. These named values allow the fields to be accessed as attributes, or for the line to be converted
    into a dictionary."""

    # All imported Python modules are singletons. Therefore, this value is a singleton.
    schemas: SchemaCollection = schema_collection


    @property
    def phonenumber(self) -> Optional[str]:
        """Override dynamically generated self.phonenumber to provide proper formatting."""
        _phonenumber = self.get("phonenumber")
        if _phonenumber:
            return format_phone_number(_phonenumber)
        return None

    @property
    def zipcode(self) -> Optional[str]:
        """Override dynamically generated self.zipcode to provide proper formatting."""
        _zipcode = self.get('zipcode')
        if _zipcode:
            _zipcode = get_only_digits(_zipcode)
            return _zipcode
        return None
