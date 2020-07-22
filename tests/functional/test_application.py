import os
from rolodex.application import application


def test_application(named_temporary_file, data_csv_path, data_json_path, hash_sha1):
    named_temporary_file.close()
    result = application(
        source=data_csv_path,
        source_storage_type='local',
        destination=named_temporary_file.name,
        destination_storage_type='local')
    assert result
    assert hash_sha1(data_json_path) == hash_sha1(named_temporary_file.name)
    os.remove(named_temporary_file.name)
