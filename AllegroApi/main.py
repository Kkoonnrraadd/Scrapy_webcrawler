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

def get_response_seller( phrase, sellerId, limit=5, searchMode="REGULAR" ):
    status_code, json_data = RestApi.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'seller.id': sellerId,
                'limit': limit,
                'searchMode': searchMode
                    }
    )
    return status_code, json_data

def get_ex_seller_data(phase, sellerId): #funkcja ktora ma na celu sprawdzenie czy produkt o nazwie phase nie znajduje sie u innych sprzedawcow
    #jezeli sie znajduje to zwraca item i mozna tu np porownywac te produkty po cenie
    status_code, json_data = get_response_seller(phase, sellerId)
    item_list_to_compare=data_extractor.extract_data_seller(json_data)
    save_json(item_list_to_compare)

def insert_count(): #user podaje liczbe produktow
    try:
        product_count = int(input("Wpisz ilość produktów:\n"))
        if product_count < 0 or product_count > 5:
            print("Podano nieprawidłową wartość")
            return insert_count()
        else:
            return product_count
    except ValueError:
        print("Podano nieprawidłową wartość")
        return insert_count()

def input_user(): #user wprowadza produkty
    for i in range(products_count):
        k = input("Enter the name: ")
        input_table.append(k)
        get_extracted_data(k)

input_table=[]
products_count=insert_count()
input_user()

seller_table = checkSeller.getSellers() #tej tablicy
checkSeller.show()
for i in input_table:
    get_ex_seller_data(i,'49703356') # tutaj jak wprowadzisz z palca seller.id to smiga, ale jak juz przekazuje z tej tablicy
#to wyszukuje tak jakby wgl nie bylo tego parametru podanego
#np. seller.id "49703356" i phase kokos i cokolwiek
#wynik zwraca duzo dla hasla kokos i czegos tam, a zapytanie wyciaga tylko dwa recordu w ktorych sie zgadza phase i seller.id


