__all__ = ['ListOfStringsTokenizer']


class ListOfStringsTokenizer:
    """Tokenizes a list of strings into a list of list of strings."""
    seperator = ' '
    tokenized_line_klass = list
    tokenized_line_collection_klass = list

    def __init__(self, lines):
        self.lines = lines

    def tokenize_lines(self):
        return self.tokenized_line_collection_klass([self._tokenize_line(_) for _ in self.lines])

    def _tokenize_line(self, val, token=None):
        if token is None:
            token = self.seperator
        return self.tokenized_line_klass(val.split(token))
