import unittest
import csv
import json

class TestData(unittest.TestCase):
    def test_csv_columns(self):
        with open('profiles1.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            self.assertEqual(len(headers), 12, "CSV should have 12 columns")

    def test_csv_rows(self):
        with open('profiles1.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = sum(1 for row in reader) - 1  # منهای هدر
            self.assertGreater(rows, 900, "CSV should have more than 900 rows")

    def test_json_rows(self):
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertGreater(len(data), 900, "JSON should have more than 900 rows")

    def test_json_properties(self):
        expected_keys = [
            "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
        ]
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for record in data:
                self.assertEqual(list(record.keys()), expected_keys, "JSON record missing properties")

if __name__ == '__main__':
    unittest.main()