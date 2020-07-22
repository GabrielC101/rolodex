__all__ = ['CSVReaderBase', 'CSVReader']

from pathlib import Path
from typing import Union, List

from rolodex.settings import CSV_ENCODING
from rolodex.list_schemas.tokenizers import ListOfStringsTokenizer
from rolodex.tokenizers import LineTokenizer


class CSVReaderBase:

    tokenizer = ListOfStringsTokenizer

    def read(self, source: Union[str, Path], storage_type='local'):
        if storage_type == 'local':
            return self.read_from_local_file(source)
        elif storage_type == 's3':
            return self.read_from_s3(source)
        elif storage_type == 'gcloud_bucket':
            return self.read_from_gcloud_bucket(source)
        raise ValueError(f'Currently do not support storage type {storage_type}')

    def read_from_local_file(self, source: Union[str, Path]) -> List[str]:
        source_path: Path = Path(source)
        lines = []
        if source_path.exists():
            buffer = open(str(source_path.absolute()), encoding=CSV_ENCODING)
            for line in buffer:
                lines.append(line.strip())
            if self.tokenizer:
                return self.tokenizer(lines).tokenize_lines()
            return lines

        raise ValueError(f'Cannot find CSV file at {source}')

    def read_from_s3(self, *args, **kwargs):
        """Not necessary. Implement in the future."""
        raise NotImplementedError()

    def read_from_gcloud_bucket(self, *args, **kwargs):
        """Not necessary. Implement in the future."""
        raise NotImplementedError()


class CSVReader(CSVReaderBase):
    """Reads and tokenizes CSVs."""

    tokenizer = LineTokenizer

