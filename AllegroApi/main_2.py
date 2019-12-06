import time

from pyAllegro.api import AllegroRestApi
from AllegroApi import extractions
from AllegroApi import fetch_module

time_start = time.time()

RestApi = AllegroRestApi()


def prepare_query():
    # przygotuj jakiegos dicta czy cos, co można byłoby wciągnąć do zapytania
    # szukane_dummy_dict = {'kabel do słuchawek recabling': [5, 70], 'Trąbka eustachiusza': [15, 300], 'Ostrze skalpel 100 szt. nr 11': [0, 25]}
    szukane_dummy_dict = {'kasza jaglana': [0, 100], 'mąka gryczana': [0, 100], 'mak biały': [0, 100]}
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

        print('PARENT SEARCH: \t{}'.format(search_item_name))
        # print('\t-------------------FIRST ORDER DATA: {}'.format(first_order_data[search_item_name]))

        keys = set(dict.keys(first_order_data))
        excludes = set([search_item_name])
        for found_item in first_order_data[search_item_name]:
            # print(found_item)
            seller_id = found_item['seller']

            for other_inputed_item in keys.difference(excludes):
                min_price, max_price = get_price_range(input_search_parameters[other_inputed_item])
                # szukaj u sprzedawcy o seller_id, itemu o nazwie other_inputed_item i min i max cenie.
                returned_raw_data = fetch_module.get_seller_response(RestApi, other_inputed_item, seller_id, limit=1,
                                                                     maximum_price=max_price, minimum_price=min_price)
                extracted_second_order_search_output = extractions.extract_valuable_info_from_raw_data(
                    returned_raw_data)
                try:
                    print('\t\t Found {} item for parent_item_id = {} with id ='
                          ' {} in {} staff and price {}: '.format(other_inputed_item,
                                                                  found_item['offer_id'],
                                                                  extracted_second_order_search_output[0]['offer_id'],
                                                                  # extracted_search_output[other_inputed_item]['offer_id'],
                                                                  seller_id,
                                                                  extracted_second_order_search_output[0][
                                                                      'item_price']))
                    # print('\t\t\t------------------------------\n{}'.format(extracted_search_output))
                except IndexError:
                    pass


def get_data():
    multi_search_parameters = prepare_query()
    first_order_data = {}
    for item_name in multi_search_parameters:
        haslo = item_name
        min_price, max_price = get_price_range(multi_search_parameters[haslo])
        returned_search_raw_data = fetch_module.get_response(RestApi, haslo, minimum_price=min_price,
                                                             maximum_price=max_price)

        list_of_items_returned_for_searched_item = extractions.extract_valuable_info_from_raw_data(
            returned_search_raw_data)
        first_order_data[item_name] = list_of_items_returned_for_searched_item
    # {szukany1: [znaleziony1, znaleziony2, ...], szukany2: [znaleziony1, znaleziony2, ...], ...}

    look_for_other_items_in_sellers(first_order_data, multi_search_parameters)
    # utils.save_json(first_order_data)


get_data()
print('\n\n---------------------------------------\n\tTOTAL TIME OF EXECUTION: {}'.format(time.time() - time_start))
