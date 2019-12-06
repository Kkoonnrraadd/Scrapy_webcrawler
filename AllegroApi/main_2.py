import time

from pyAllegro.api import AllegroRestApi
from AllegroApi import extractions
from AllegroApi import fetch_module
from AllegroApi import utils
time_start = time.time()

RestApi = AllegroRestApi()


def prepare_query():
    # przygotuj jakiegos dicta czy cos, co można byłoby wciągnąć do zapytania
    # szukane_dummy_dict = {'kabel do słuchawek recabling': [5, 70], 'Trąbka eustachiusza': [15, 300], 'Ostrze skalpel 100 szt. nr 11': [0, 25]}
    # szukane_dummy_dict = {'lampka led dla roślin': [10, 25], 'zamgławiacz fogger': [5, 25], 'płyn do soczewek 500 ml': [0, 12],
    #                       'nóż do szkła': [15,50], 'kindle keyboard': [60,150]}

    # szukane_dummy_dict = {'zarowka led dla roslin': [10, 25], 'zamglawiacz fogger': [5, 75], 'plyn do soczewek 500 ml': [0, 20],
    #                       'nóż do szkła': [15, 50], 'kindle': [60, 350]}

    # szukane_dummy_dict = {'daktyle 1kg': [3, 25], 'Rodzynki 1kg': [5, 25],
    #                       'żurawina suszona 1kg': [5, 30],
    #                       'Kurkuma 250g': [0, 15], 'pieprz czarny 100g': [0, 20]}

    szukane_dummy_dict = {'daktyle 1kg': [0, 11], 'kmin rzymski 250g': [0, 6],
                          'kolendra 250g': [0, 6],
                          'Orzechy arachidowe 1kg': [0, 15]}
    return szukane_dummy_dict


def get_price_range(min_max_price):
    # trzeba pamietac, zeby cena minimalna zawsze była w zakresie [0;max_price]
    min_price = min_max_price[0]
    max_price = min_max_price[1]
    return min_price, max_price


def look_for_other_items_in_sellers(first_order_data, input_search_parameters):
    # item_subitem = {}
    sellers_found = set()
    DUZY_DICT = {}
    print('\twywolanie look_for_other_items_in_sellers')
    print('\t\tinicjalizacja DUZY_DICT')

    for search_item_name in first_order_data:
        print('\t\t\tsearch_item_name: {}'.format(search_item_name))
        min_price, max_price = get_price_range(input_search_parameters[search_item_name])
        # dla kazdego hasla i zakresu cenowego, ktory zdefiniowalismy,
        # dla kazdego itemu znalezionego
        # dla kazdego sprzedawcy tego itemu
        # szukaj itemow pasujacych do pozostalych szukanych fraz

        # print('PARENT SEARCH: \t{}'.format(search_item_name))
        # print('\t-------------------FIRST ORDER DATA: {}'.format(first_order_data[search_item_name]))
        keys = set(dict.keys(first_order_data))
        print('\t\t\tstan_kluczy: {}'.format(keys))
        excludes = set([search_item_name])
        print('\t\t\texcludes: {}'.format(search_item_name))

        for found_item in first_order_data[search_item_name]:
            seller_id = found_item['seller']
            print('\t\t\t\tseller_id: {}'.format(seller_id))
            # print(found_item)
            sredni_dict = {}
            maly_sredni_dict = {}
            print('')

            if seller_id not in sellers_found:  # to po to, żeby nie duplikować.
                maly_sredni_dict['id'] = found_item['offer_id']
                maly_sredni_dict['price'] = found_item['item_price']
                maly_sredni_dict['name'] = found_item['item_name']
                maly_sredni_dict['link'] = found_item['item_link']
                maly_sredni_dict['delivery_price'] = found_item['delivery_price']
                sredni_dict[search_item_name] = maly_sredni_dict
                print('\t\t\t\t\tmaly_sredni_dict = {}'.format(maly_sredni_dict))
                print('\t\t\t\t\tsredni_dict({}) = {}'.format(search_item_name, sredni_dict))

                # Wybieramy najtańszy przedmiot każdego sprzedającego
                sellers_found.add(seller_id)

                for other_inputed_item in keys.difference(excludes):
                    print('\t\t\t\t\t\tother_inputed_item_loop')
                    min_price, max_price = get_price_range(input_search_parameters[other_inputed_item])
                    # szukaj u sprzedawcy o seller_id, itemu o nazwie other_inputed_item i min i max cenie.
                    returned_raw_data = fetch_module.get_seller_response(RestApi, other_inputed_item, seller_id, limit=1,
                                                                             maximum_price=max_price, minimum_price=min_price)
                    extracted_second_order_search_output = extractions.extract_valuable_info_from_raw_data(returned_raw_data)
                    try:

                        #  zapisywanie znalezionych wyników,
                        #  tj. id_sprzedawcy: {nazwa przedmiotu_1: {id:id_przedmiotu, link:link_do_przedmiotu,
                        #  cena: cena_przedmiotu, dostawa: cena_dostawy_przedmiotu}, nazwa_przedmiotu_2...}
                        #  ??????max_cena_przesylki: max_cena_przesyłki, cena_wszystkiego: cena_sumaryczna}???? czy liczyć osobno?

                        # w tej pętli jeśli znajdziemy jakiś przedmiot będący u sprzedawcy z pętli powyżej,
                        # robimy z niego dicta i dodajemy do powyższego dicta

                        maly_dict = {}
                        maly_dict['id'] = extracted_second_order_search_output[0]['offer_id']
                        maly_dict['price'] = extracted_second_order_search_output[0]['item_price']
                        maly_dict['name'] = extracted_second_order_search_output[0]['item_name']
                        maly_dict['link'] = extracted_second_order_search_output[0]['item_link']
                        maly_dict['delivery_price'] = extracted_second_order_search_output[0]['delivery_price']
                        sredni_dict[other_inputed_item] = maly_dict
                        print('\t\t\t\t\t\tsredni_dict({}) = {}'.format(other_inputed_item, sredni_dict))

                        DUZY_DICT[seller_id] = sredni_dict
                        print('\t\t\t\t\t\tDUZY_DICT = {}'.format(DUZY_DICT))
                    except IndexError:
                        pass
    return DUZY_DICT


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
    utils.save_json(first_order_data, filename='first_order.json')
    OUTPUT = look_for_other_items_in_sellers(first_order_data, multi_search_parameters)
    utils.save_json(OUTPUT)


get_data()
print('\n\n---------------------------------------\n\tTOTAL TIME OF EXECUTION: {}'.format(time.time() - time_start))
