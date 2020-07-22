"""Schema objects for fixed lengths lists."""

__all__ = ['SchemaOne', 'SchemaTwo', 'SchemaThree', 'schema_collection']


from typing import List

from rolodex.list_schemas.fields import Field
from rolodex.list_schemas.schemas import SchemaBase, SchemaCollection


class SchemaOne(SchemaBase):
    """Defines a fixed list schema."""

    fields: List[Field] = [
        Field('rolodex.validators.is_name_or_color', 'lastname'),
        Field('rolodex.validators.is_name_or_color', 'firstname'),
        Field('rolodex.validators.is_phone_number', 'phonenumber'),
        Field('rolodex.validators.is_name_or_color', 'color'),
        Field('rolodex.validators.is_zip_code', 'zipcode')
    ]
    name = 'one'


class SchemaTwo(SchemaBase):
    """Defines a fixed list schema."""

    fields: List[Field] = [
        Field('rolodex.validators.is_name_or_color', 'firstname'),
        Field('rolodex.validators.is_name_or_color', 'lastname'),
        Field('rolodex.validators.is_name_or_color', 'color'),
        Field('rolodex.validators.is_zip_code', 'zipcode'),
        Field('rolodex.validators.is_phone_number', 'phonenumber'),
    ]
    name = 'two'


class SchemaThree(SchemaBase):
    """Defines a fixed list schema."""

    fields: List[Field] = [
        Field('rolodex.validators.is_name_or_color', 'firstname'),
        Field('rolodex.validators.is_name_or_color', 'lastname'),
        Field('rolodex.validators.is_zip_code', 'zipcode'),
        Field('rolodex.validators.is_phone_number', 'phonenumber'),
        Field('rolodex.validators.is_name_or_color', 'color'),
    ]
    name = 'three'


# Schema collection. Schemas in order of preference, that is, if a line is validated as True by multiple schemas,
# it is assumed the first schema to validate True is the correct schema.
schema_collection: SchemaCollection = SchemaCollection([
    SchemaOne(),
    SchemaTwo(),
    SchemaThree()
])
