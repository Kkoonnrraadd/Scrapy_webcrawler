from pyAllegro.api import AllegroRestApi
import json


RestApi = AllegroRestApi()

# RestApi.load_token()

status_code, json_data = RestApi.resource_get(
        resource_name='/offers/listing',
        params={'phrase': 'Dell Inspiron 7347 i5-4210U/8GB/256/Win8 FHD Dotyk',
                'limit' : 1}
        )

with open('zapytanie.json', 'w') as zapytanie:
    json.dump(json_data, zapytanie)