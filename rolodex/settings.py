import os
from pathlib import Path
from sys import getdefaultencoding

PROJECT_APP_PATH: Path = Path(__file__).absolute().parent
PROJECT_APP = PROJECT_APP_PATH.name

BASE_DIR = PROJECT_APP_PATH.parent
PROJECT_ROOT = BASE_DIR

SOURCE_FILE_NAME = 'data.csv'
DESTINATION_FILE_NAME = 'data.json'

CSV_ENCODING = getdefaultencoding()


SOURCE_FILE_PATH = PROJECT_ROOT.joinpath(SOURCE_FILE_NAME)
DESTINATION_FILE_PATH = PROJECT_ROOT.joinpath(DESTINATION_FILE_NAME)

SOURCE_STRING = os.environ.get('SOURCE_STRING', str(SOURCE_FILE_PATH))
SOURCE_STORAGE_TYPE = os.environ.get('SOURCE_STORAGE_TYPE', 'local')
DESTINATION_STRING = os.environ.get('DESTINATION_STRING', str(DESTINATION_FILE_PATH))
DESTINATION_STORAGE_TYPE = os.environ.get('DESTINATION_STORAGE_TYPE', 'local')


local_settings_file_path = PROJECT_APP_PATH.joinpath("local_settings.py")

if local_settings_file_path.exists():
    exec(local_settings_file_path.open("rb").read())

