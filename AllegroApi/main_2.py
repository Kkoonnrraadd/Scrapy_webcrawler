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
    szukane_dummy_dict = {'kabel do słuchawek recabling': [5, 70], 'Trąbka eustachiusza': [15, 300], 'Ostrze skalpel 100 szt. nr 11': [0, 25]}
    return szukane_dummy_dict


def get_price_range(min_max_price):
    # trzeba pamietac, zeby cena minimalna zawsze była w zakresie [0;max_price]
    min_price = min_max_price[0]
    max_price = min_max_price[1]
    return min_price, max_price


def look_for_other_items_in_sellers(first_order_data, input_search_parameters):
    for search_item_name in first_order_data:
        min_price, max_price = get_price_range(input_search_parameters[search_item_name])
        # dla kazdego hasla i zakresu cenowego, ktory zdefiniowalismy,
        # dla kazdego itemu znalezionego
        # dla kazdego sprzedawcy tego itemu
        # szukaj itemow pasujacych do pozostalych szukanych fraz

        keys = set(dict.keys(first_order_data))
        excludes = set(search_item_name)

        for found_item in first_order_data[search_item_name]:
            seller_id = found_item['seller']['id']
            for other_inputed_item in keys.difference(excludes):
                min_price, max_price = get_price_range(input_search_parameters[other_inputed_item])
                # szukaj u sprzedawcy o seller_id, itemu o nazwie other_inputed_item i min i max cenie.

            # trzeba to będzie jeszcze zapisać



        # print(search_item_name)


def get_data():
    multi_search_parameters = prepare_query()
    first_order_data = {}
    for item_name in multi_search_parameters:
        haslo = item_name
        min_price, max_price = get_price_range(multi_search_parameters[haslo])
        returned_search_raw_data = fetch_module.get_response(RestApi, haslo, minimum_price=min_price, maximum_price=max_price)
        list_of_items_returned_for_searched_item = extractions.extract_valuable_info_from_raw_data(returned_search_raw_data)
        first_order_data[item_name] = list_of_items_returned_for_searched_item
    # {szukany1: [znaleziony1, znaleziony2, ...], szukany2: [znaleziony1, znaleziony2, ...], ...}
    look_for_other_items_in_sellers(first_order_data, multi_search_parameters)
    # utils.save_json(first_order_data)
get_data()


