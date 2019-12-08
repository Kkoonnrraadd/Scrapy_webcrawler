import time

from pyAllegro.api import AllegroRestApi
from AllegroApi import extractions
from AllegroApi import fetch_module
from AllegroApi import utils

time_start = time.time()

RestApi = AllegroRestApi()


def prepare_query():
    # szukane_dummy_dict = {'zarowka led dla roslin': [10, 25], 'zamglawiacz fogger': [5, 75],
    #                       'plyn do soczewek 500 ml': [0, 20]}

    # szukane_dummy_dict = {'daktyle 1kg': [3, 25], 'Rodzynki 1kg': [5, 25],
    #                       'żurawina suszona 1kg': [5, 30],
    #                       'Kurkuma 250g': [0, 15], 'pieprz czarny 100g': [0, 20]}

    szukane_dummy_dict = {'daktyle 1kg': [0, 11],
                          'Orzechy arachidowe 1kg': [0, 15],
                          'Kurkuma 250g': [0, 15]}
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
    # print('\twywolanie look_for_other_items_in_sellers')
    # print('\t\tinicjalizacja DUZY_DICT')

    for search_item_name in first_order_data:
        # print('\t\t\tsearch_item_name: {}'.format(search_item_name))
        min_price, max_price = get_price_range(input_search_parameters[search_item_name])
        # dla kazdego hasla i zakresu cenowego, ktory zdefiniowalismy,
        # dla kazdego itemu znalezionego
        # dla kazdego sprzedawcy tego itemu
        # szukaj itemow pasujacych do pozostalych szukanych fraz

        # print('PARENT SEARCH: \t{}'.format(search_item_name))
        # print('\t-------------------FIRST ORDER DATA: {}'.format(first_order_data[search_item_name]))
        keys = set(dict.keys(first_order_data))
        # print('\t\t\tstan_kluczy: {}'.format(keys))
        excludes = set([search_item_name])
        # print('\t\t\texcludes: {}'.format(search_item_name))

        for found_item in first_order_data[search_item_name]:
            seller_id = found_item['seller']
            # print('\t\t\t\tseller_id: {}'.format(seller_id))
            # print(found_item)
            sredni_dict = {}
            maly_sredni_dict = {}
            # print('')
            maly_sredni_dict['id'] = found_item['offer_id']
            maly_sredni_dict['price'] = found_item['item_price']
            maly_sredni_dict['name'] = found_item['item_name']
            maly_sredni_dict['link'] = found_item['item_link']
            maly_sredni_dict['delivery_price'] = found_item['delivery_price']
            maly_sredni_dict['seller'] = found_item['seller']

            sredni_dict[search_item_name] = maly_sredni_dict

            # print('\t\t\t\t\tmaly_sredni_dict = {}'.format(maly_sredni_dict))
            # print('\t\t\t\t\t------sredni_dict[{}] = {}'.format(search_item_name, sredni_dict[search_item_name]))

            if seller_id not in sellers_found:  # to po to, żeby nie duplikować.

                # print('\t\t\t\t\tsredni_dict({}) = {}'.format(search_item_name, sredni_dict))

                # Wybieramy najtańszy przedmiot każdego sprzedającego
                sellers_found.add(seller_id)

                for other_inputed_item in keys.difference(excludes):
                    # print('\t\t\t\t\t\tother_inputed_item_loop')
                    min_price, max_price = get_price_range(input_search_parameters[other_inputed_item])
                    # szukaj u sprzedawcy o seller_id, itemu o nazwie other_inputed_item i min i max cenie.
                    returned_raw_data = fetch_module.get_seller_response(RestApi, other_inputed_item, seller_id,
                                                                         limit=1,
                                                                         maximum_price=max_price,
                                                                         minimum_price=min_price)
                    extracted_second_order_search_output = extractions.extract_valuable_info_from_raw_data(
                        returned_raw_data)
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
                        maly_dict['seller'] = extracted_second_order_search_output[0]['seller']
                        sredni_dict[other_inputed_item] = maly_dict
                        # print('\t\t\t\t\t\tsredni_dict({}) = {}'.format(other_inputed_item, sredni_dict))
                        # print('\t\t\t\t\t\t-------------TU_DODAJE_SIE_SREDNI_DICT_DO_DUZEGO')
                        DUZY_DICT[seller_id] = sredni_dict
                    except IndexError:
                        # DUZY_DICT[seller_id] = sredni_dict
                        pass
                DUZY_DICT[seller_id] = sredni_dict
    return DUZY_DICT


def get_most_expensive_delivery_price(delivery_price_table):
    try:
        return delivery_price_table.sort()[0]
    except TypeError:
        return delivery_price_table[0]


def get_sum_of_prices(found_items_data):
    for seller_id in found_items_data:
        total_price = 0.0
        product_price_sum = 0.0
        delivery_price_table = []
        for item in found_items_data[seller_id]:
            product_price_sum = product_price_sum + found_items_data[seller_id][item]['price']
            delivery_price_table.append(found_items_data[seller_id][item]['delivery_price'])
            total_price = product_price_sum + get_most_expensive_delivery_price(delivery_price_table)
        found_items_data[seller_id]['total_price'] = total_price
    return found_items_data


def choose_cheapest_set(data, searched_names=''):
    worek = {}
    number_of_items_searched = 0
    for keys in searched_names:
        number_of_items_searched = number_of_items_searched + 1
        worek[keys] = []
    # jeśli przeleciałeś po wszystkich itemach sprzedawcy i są wszystkie szukane - zlicz cenę i wypisz do zbioru sprzedawców
    # ze wszystkimi itemami -> sprzedawca_id = sumaryczna_cena

    # jeśli po jednym itemie od każdego sprzedawcy

    # Dla każdego sprzedawcy posiadającego przedmiot A,( b, c,...) znajdź każdego sprzedawcę posiadającego przedmiot B,
    # C, D, E, F. Dla każdej kombinacji wszystkich przedmiotów zlicz cenę i zapisz zbiór:
    # sprzedawca_1:przedmiot_A, sprzedawca_2:rpzedmiotB. Jeśli sprzedawca_1 ma przedmiot A i B,
    # to dodawaj jakoś te ceny...

    # to powinno być tak, że mamy listę zbiorów sprzedawca:przedmiot. Dla kazdego przedmiotu, dodajemy sprzedawcę, który ma przedmiot
    # po jednym tak, żeby uzyskać wszystkie możliwe sposoby połączenia (bruteforce)
    # all_possible_sets = {}
    # for searched_item in searched_names:
    #     for seller in data:
    #         if data[seller][searched_item]:
    #             all_possible_sets.append()
    #     pass
    for seller in data:
        for item in data[seller]:
            # print(data[seller][item])
            worek[item].append(data[seller][item])

    all_possible_combinations = {}
    iterator = 0

    for seller in data:
        for item in data[seller]:
            all_possible_combinations[iterator] = [data[seller][item]]
            for item2 in data[seller]:
                if item2 != item:
                    all_possible_combinations[iterator].append(data[seller][item2])
            iterator = iterator + 1

    for iterator in all_possible_combinations:
        if len(all_possible_combinations[iterator]) == number_of_items_searched:
            sellers_ids = []

            price_sum = 0
            for item in all_possible_combinations[iterator]:
                delivery_price = 0
                sum_of_delivery_price = 0
                price_sum = 0
                print(item)
                price_sum = price_sum + item['price']
                # price_sum = price_sum+all_possible_combinations[iterator][item]['price']
                sum_of_delivery_price = sum_of_delivery_price + item['delivery_price'] #all_possible_combinations[iterator][item]['delivery_price']
                for item2 in all_possible_combinations[iterator]:
                    if item != item2:
                        if item['seller'] == item2['seller']:  # all_possible_combinations[iterator][item2]['seller']:
                            delivery_price_two_max = max(item['delivery_price'], item2['delivery_price'])
                            delivery_price = max(delivery_price, delivery_price_two_max)
                            price_sum = price_sum+item2['price']
                        else:
                            sum_of_delivery_price = sum_of_delivery_price+item2['seller']
                            price_sum = price_sum+item2['price']
                sum_of_delivery_price = sum_of_delivery_price + delivery_price
            price_sum_with_delivery = sum_of_delivery_price+price_sum
            print('iterator {} price summ {}'.format(iterator, price_sum_with_delivery))

    utils.save_json(all_possible_combinations, 'all_possible.json')
    print(all_possible_combinations)



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
    OUTPUT = look_for_other_items_in_sellers(first_order_data, multi_search_parameters)
    # OUTPUT = get_sum_of_prices(OUTPUT)  # dane ze zsumowanymi cenami
    choose_cheapest_set(OUTPUT,multi_search_parameters)
    utils.save_json(OUTPUT)

    return OUTPUT


get_data()
print('\n\n---------------------------------------\n\tTOTAL TIME OF EXECUTION: {}'.format(time.time() - time_start))


# teraz fajnie byłoby mieć takie coś, żeby przelatywać po sprzedawcach i sprawdzać, które atrybuty mają z naszej listy
# jakoś zbierać to, żeby