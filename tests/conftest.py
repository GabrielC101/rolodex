import hashlib
from pathlib import Path
from sys import getdefaultencoding
from tempfile import NamedTemporaryFile

import pytest

FIXTURES_ROOT = Path(__file__).absolute().parent.joinpath('fixtures')

SOURCE_FILE_NAME = 'data.csv'
DESTINATION_FILE_NAME = 'data.json'

CSV_ENCODING = getdefaultencoding()


SOURCE_FILE_PATH = FIXTURES_ROOT.joinpath(SOURCE_FILE_NAME)
DESTINATION_FILE_PATH = FIXTURES_ROOT.joinpath(DESTINATION_FILE_NAME)


@pytest.fixture
def data_csv_path():
    return SOURCE_FILE_PATH


@pytest.fixture
def data_json_path():
    return DESTINATION_FILE_PATH


@pytest.fixture
def named_temporary_file():
    return NamedTemporaryFile(mode='wt')


@pytest.fixture
def hash_sha1():
    def _hash_sha1(file_path):
        BLOCKSIZE = 65536
        hasher = hashlib.sha1()
        with open(file_path, 'rb') as afile:
            buffer = afile.read(BLOCKSIZE)
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = afile.read(BLOCKSIZE)
        return str(hasher.hexdigest())
    return _hash_sha1