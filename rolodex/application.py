"""Main application module."""

__all__ = ['application']

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
    """
    Main application. Reads CSV, converts csv columns to JSON, accounts for errors, and writes to JSON.

    :param source: Source string. For local filesystem, absolute path. For remove systems, will vary.
    :param source_storage_type: Source system type.
    :param destination: Destination string. For local filesystem, absolute path. For remove systems, will vary.
    :param destination_storage_type: Destination system type.
    :return: True
    """

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


if __name__ == '__main__':
    application()
