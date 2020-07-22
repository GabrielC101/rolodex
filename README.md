# Rolodex application
A short term project I did a while back. Takes a csv, and converts data to json. Ignores invalid data.

## Requirements

Make sure you:
* Are running on a Linux desktop. Other platforms untested.
* Have `make` installed, and present in your PATH.
* Have Docker client installed, and present in your Path.
* Have Python 3.6 or higher as `python3` in your PATH. Python 3.7+ untested. Versions prior to 3.6, and the future 4+, 
are unlikely to work.
* Are not executing from a Python virtual environment. This is untest, and may or may not work. The Makefile is 
intended to handle virutal environments.
* Have `data.csv` located in the root `rolodex` directory.
* Have set `rolodex` root directory as your current working directory.

## Deployment

### Run in local environment

Start program by following these steps:

* The first time running the code, execute `make local-init local-test local-run`. 
This will create the virtual environment, install dependencies, and run the script.
* Inspect output. The output should include the contents of the json, plus other output.
* Inspect package at `data.json`. This will contain the results of the application
Subsequent executions can be triggered by typing `make local-run`.

### Run with docker

Start program by following these steps:
* Execute `make docker-build docker-run`.
* Inspect output. The output should include the contents of the json, plus other output.
Subsequent executions can be triggered by typing `make docker-run-application` to skip testing.

## Reusability

### List Schemes Library

To assist with reusability, the list_schemes library allows a programmer to define a tabular row as a schema, 
similar to schemas in Django Rest Framework or Marshmallow. This schema only supports fixed length, immutable lists. 
In other words, tuples, although for pragmatic reasons, they inherit from Python's `list` or `UserList` base classes.

Python lists represent data in an ordered, although unnamed, manner. the list_schemas library allows a the items in a
fixed list to correspond to both order and name.


#### Schemas

Here is an example of a Schema definition:

```python
from typing import List
from rolodex.list_schemas.fields import Field
from rolodex.list_schemas.schemas import SchemaBase, SchemaCollection

class SchemaOne(SchemaBase):

    fields: List[Field] = [
        Field('rolodex.validators.is_name_or_color', 'lastname'),
        Field('rolodex.validators.is_name_or_color', 'firstname'),
        Field('rolodex.validators.is_phone_number', 'phonenumber'),
        Field('rolodex.validators.is_name_or_color', 'color'),
        Field('rolodex.validators.is_zip_code', 'zipcode')
    ]
    name = 'one'

```

Schemas inherit from the `SchemaBase` class. They must have a `name`, and a list of `fields`. The name is an arbitrary
string, although it must be unique within a `SchemaCollection`.

### Fields

A field is an instance of the Field class. A Field takes two arguments, the first is a, validator function, 
or Django style string address to a validator function. Down the road, fields might be definable by means of settings file, 
possibly in JSON, YAML, or XML format, which is why string addresses are allowed. The other argument is a name for the
field. This is an arbitrary string that must be unique. The name allows identification of the value once lines are parsed.

### Validators
A validator must receive a string, and return a True or False, depending on whether the string is valid.



### SchemaCollections
List schemas upports the concept of `SchemaCollection`, a tabular data structure (such as a CSV) to have row that
correspond to multiple conflicting schemas, albeit of the same length.

Here is an example of a SchemaCollection:

```python

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


schema_collection: SchemaCollection = SchemaCollection([
    SchemaOne(),
    SchemaTwo(),
    SchemaThree()
])

```

SchemaCollections are simply a collection of schemas, collected in order of application. When processing a line, 
the schema collection will assume the line should be validated by the first schema for which it is valid, that is,
for the first schema for which all validators are return True.

After the schema collection, and it's component schemas are defined, it is time to define how the line "should look".
This is done using TokenizedLines. 

### Tokenized Lines

Tokenized lines inherit from the `AbstractTokenizedLine` class. The class must have a schemas attribute that consists
of a populated `SchemaCollection`.

Once the lines are tokenized, you can access the fields using the names defined in the Schemas. That is all that is 
necessary, however if you want the value of a field to be different from what is consumed,
you can override them using properties, accessing the values via `self.get(value)`.

For example:

```python

from typing import Dict, List, Optional

from rolodex.list_schemas.schemas import SchemaCollection
from rolodex.list_schemas.structs import AbstactTokenizedLine, AbstractTokenizedLineCollection
from rolodex.schemas import schema_collection
from rolodex.utils import format_phone_number, get_only_digits


class TokenizedLine(AbstactTokenizedLine):

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

```

### Tokenizers

Once the TokenizedLine is defined. The tokenizer must be defined. The tokenizer inherits from the ListOfStringsTokenizer
class. The ListOfStringsTokenizer class be used directly, or the defaults may be overridden.

```python
from rolodex.list_schemas.tokenizers import ListOfStringsTokenizer
from rolodex.stucts import TokenizedLine, TokenizedLineCollection

class LineTokenizer(ListOfStringsTokenizer):
    """Tokenizes a list of strings, into a list of list of strings, using customer settings."""

    seperator = ', '
    tokenized_line_klass = TokenizedLine
    tokenized_line_collection_klass = TokenizedLineCollection
```

### CSV Reader

Ultimately, the CSV Reader must be defined. It inherits from the CSVReaderBase class. The line_tokenizer class
attribute should be assigned as the line tokenizer defined above.

### Application

And now you're ready to create an application. For example:

````python
from rolodex.settings import SOURCE_STORAGE_TYPE, SOURCE_STRING, DESTINATION_STORAGE_TYPE, DESTINATION_STRING
from rolodex.stucts import TokenizedLineCollection
from rolodex.utils import name_sort_key
from rolodex.writers import JSONWriter
from rolodex.readers import CSVReader

def application(
        source=SOURCE_STRING,
        source_storage_type=SOURCE_STORAGE_TYPE,
        destination=DESTINATION_STRING,
        destination_storage_type=DESTINATION_STORAGE_TYPE) -> bool:


    # Reads lines from file.
    csv_reader = CSVReader()
    tokenized_lines: TokenizedLineCollection = csv_reader.read(source, storage_type=source_storage_type)

    # Creates result and sortes entries
    result = {
        'entries': sorted(tokenized_lines.valid_dicts, key=name_sort_key),
        'errors': tokenized_lines.error_indexes
    }

    # Saves result as JSON
    writer = JSONWriter()
    writer.save(result)
    writer.write(destination, storage_type=destination_storage_type)
    return True
````

