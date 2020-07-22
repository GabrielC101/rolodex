from rolodex.readers import CSVReader


def test_csv_reader(data_csv_path):
    csv_reader = CSVReader()
    csv_lines = csv_reader.read(data_csv_path)
    assert len(csv_lines) == 64
