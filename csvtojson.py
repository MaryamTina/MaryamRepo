import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r', encoding='utf-8') as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for row in csv_reader:
            data.append(row)
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    csv_to_json('profiles1.csv', 'data.json')