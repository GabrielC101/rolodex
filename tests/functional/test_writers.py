import os
from rolodex.writers import JSONWriter
from rolodex.readers import CSVReader


def test_json_writer(named_temporary_file):
    named_temporary_file.close()
    json_writer = JSONWriter()
    json_data = {'name': 'David'}
    json_writer.save(json_data)
    json_writer.write(named_temporary_file.name)

    csv_reader = CSVReader()
    csv_lines = csv_reader.read(named_temporary_file.name)
    os.remove(named_temporary_file.name)
    assert len(csv_lines) == 3