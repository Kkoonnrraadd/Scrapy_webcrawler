from pyAllegro.api import AllegroRestApi
import json
from AllegroApi import extractions
from AllegroApi import checkSeller
from AllegroApi import fetch_module
from AllegroApi import utils
from AllegroApi import user_interaction

RestApi = AllegroRestApi()


def prepare_query():
    # przygotuj jakiegos dicta czy cos, co można byłoby wciągnąć do zapytania
    szukane_dummy_dict = {'Kasza bezglutenowa pszenna': [5, 30], 'Trąbka eustachiusza': [15, 300], 'Ostrze skalpel 100 szt. nr 11': [0, 25]}
    return szukane_dummy_dict


def get_price_range(min_max_price):
    # trzeba pamietac, zeby cena minimalna zawsze była w zakresie [0;max_price]
    min_price = min_max_price[0]
    max_price = min_max_price[1]
    return min_price, max_price


def get_data():
    multi_search_parameters = prepare_query()
    searched_item_name__items_found_data = {}
    for item_name in multi_search_parameters:
        haslo = item_name
        print('doszedlem')
        min_price, max_price = get_price_range(multi_search_parameters[haslo])
        returned_search_raw_data = fetch_module.get_response(RestApi, haslo, minimum_price=min_price, maximum_price=max_price)
        list_of_items_returned_for_searched_item = extractions.extract_valuable_info_from_raw_data(returned_search_raw_data)
        searched_item_name__items_found_data[item_name] = list_of_items_returned_for_searched_item
    # {szukany1: [znaleziony1, znaleziony2, ...], szukany2: [znaleziony1, znaleziony2, ...], ...}
    utils.save_json(searched_item_name__items_found_data)
get_data()