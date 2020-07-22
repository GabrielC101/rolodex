__all__ = ['JSONWriter']

import json
from io import StringIO
from pathlib import Path
from typing import Union

from rolodex.settings import CSV_ENCODING


class JSONWriter:
    """Writes a JSON file."""

    def __init__(self, buffer=None, encoding=CSV_ENCODING):
        if not buffer:
            buffer = StringIO()
        self.buffer = buffer
        self.encoding = encoding

    def save(self, data, sort_keys=True, indent=2, **kwargs):
        json.dump(data, self.buffer, sort_keys=sort_keys, indent=indent, **kwargs)
        return True

    def write_to_local_file(self, destination: Union[str, Path]):
        """
        Writes data to local file.

        :param destination: file path to save data
        :return: True
        """
        destination = Path(destination)
        destination.write_text(self.buffer.getvalue(), encoding=self.encoding)
        return True

    def write_to_s3(self, *args, **kwargs):
        raise NotImplementedError()

    def write_to_gcloud_bucket(self, *args, **kwargs):
        raise NotImplementedError()

    def write(self, destination: Union[str, Path], storage_type='local'):
        if storage_type == 'local':
            return self.write_to_local_file(destination)
        elif storage_type == 's3':
            return self.write_to_s3(destination)
        elif storage_type == 'gcloud_bucket':
            return self.write_to_gcloud_bucket(destination)
        raise ValueError(f'Currently do not support storage type {storage_type}')