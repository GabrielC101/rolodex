"""Tokenizers. Transformers that split text into data objects."""

__all__ = ['LineTokenizer']

from rolodex.list_schemas.tokenizers import ListOfStringsTokenizer
from rolodex.stucts import TokenizedLine, TokenizedLineCollection


class LineTokenizer(ListOfStringsTokenizer):
    """Tokenizes a list of strings, into a list of list of strings, using customer settings."""

    seperator = ', '
    tokenized_line_klass = TokenizedLine
    tokenized_line_collection_klass = TokenizedLineCollection
