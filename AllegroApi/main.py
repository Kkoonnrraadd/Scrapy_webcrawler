from pyAllegro.api import AllegroRestApi
import json
from AllegroApi import data_extractor
from AllegroApi import checkSeller
RestApi = AllegroRestApi()
# RestApi.load_token()

# Brakuje jeszcze:
# wyboru minimalnej ceny przedmiotow poszukiwanych
# parsowania listy przedmiotow i odpowiedniego zapisu odpowiedzi
# wybierania sprzedawcow z list i sprawdzania u nich ofert
# liczenia lacznej ceny i zwracania odpowiednio posortowanych odpowiedzi
# GUI/cokolwiek


def get_response(phrase, limit=10, sorting='+price', minimum_price=0, maximum_price=999999999):
    status_code, json_data = RestApi.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'limit': limit,
                'sort': sorting,
                'sellingMode.price.amount.gte': int(minimum_price),  # nie dziala jeszcze
                'sellingMode.price.amount.lte': int(maximum_price),  # nie dziala jeszcze
                'sellingMode.format': "BUY_NOW"}
    )
    return status_code, json_data


def save_json(json_data, filename='zapytanie.json'):
    with open(filename, 'w') as zapytanie:
        json.dump(json_data, zapytanie)


def get_extracted_data(phrase, limit=20, sorting='+price', minumum_price=0, maximum_price=999999999):
    status_code, json_data = get_response(phrase, limit, sorting, minumum_price, maximum_price)
    # save_json(json_data, filename='odpowiedz_surowa.json')
    item_list = data_extractor.extract_data(json_data)
    save_json(item_list)


def get_price_only(list_of_items):
    list_of_prices = []
    for item in list_of_items:
        list_of_prices.append(float(item['item_price']))
    list_of_prices.sort()
    return list_of_prices

def get_response_seller(phrase,sellerId, limit=5,searchMode="REGULAR"):
    status_code, json_data = RestApi.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'seller.id': sellerId,
                'limit': limit,
                'searchMode': searchMode
                    }
    )

    return status_code, json_data

def get_ex_seller_data(phase,sellerId):
    status_code, json_data = get_response_seller(phase,sellerId)
    data_extractor.extract_data_seller(json_data)


input_table=[]
product_count=input("Enter count: ")

for i in range(int(product_count)):
    k=input("Enter the name: ")
    input_table.append(k)
    get_extracted_data(k)

seller_table=checkSeller.getSellers()
checkSeller.show()

for i in input_table:
    print(seller_table[0])
    print(i)
    get_ex_seller_data(i,"34788")   # tutaj nie dziala, kiedy chce z tablic przekazac, tylko z palca dziala

