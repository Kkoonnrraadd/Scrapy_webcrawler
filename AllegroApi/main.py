from pyAllegro.api import AllegroRestApi
import json


RestApi = AllegroRestApi()
# RestApi.load_token()


def get_response(phrase, limit=10, sorting='+price'):
    status_code, json_data = RestApi.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'limit': limit,
                'sort': sorting}
    )
    return status_code, json_data


def save_json(json_data, filename='zapytanie.json'):
    with open(filename, 'w') as zapytanie:
        json.dump(json_data, zapytanie)


def get_extracted_data(phrase):
    status_code, json_data = get_response(phrase, limit=40)
    print(type(json_data))
    for typ_oferty in json_data['items']:
        print(typ_oferty)
        for oferty in json_data['items'][typ_oferty]:
            print(oferty)
    # save_json(json_data['items'])

get_extracted_data('wibrator analny')