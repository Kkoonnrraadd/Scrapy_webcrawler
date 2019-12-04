import json


def save_json(json_data, filename='zapytanie.json'):
    with open(filename, 'w') as zapytanie:
        json.dump(json_data, zapytanie)
