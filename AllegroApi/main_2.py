import time
import itertools
from pyAllegro.api import AllegroRestApi
from AllegroApi import extractions
from AllegroApi import fetch_module
from AllegroApi import utils
from AllegroApi import user_interaction
time_start = time.time()

RestApi = AllegroRestApi()


def prepare_query():
    search_parameters = {}
    count = user_interaction.insert_count()  # liczba od usera
    for i in range(count):
        input_parameters = user_interaction.input_user()
        search_parameters.update(input_parameters)
    return search_parameters  # zwraca parametry


def get_price_range_and_state(min_max_price):
    min_price = min_max_price[0]
    max_price = min_max_price[1]
    state = min_max_price[2]
    return min_price, max_price, state


def look_for_other_items_in_sellers(first_order_data, input_search_parameters):
    sellers_found = set()
    DUZY_DICT = {}

    for search_item_name in first_order_data:
        keys = set(dict.keys(first_order_data))
        excludes = set([search_item_name])

        for found_item in first_order_data[search_item_name]:
            seller_id = found_item["seller"]

            sredni_dict = {}
            maly_sredni_dict = {}
            maly_sredni_dict["id"] = found_item["offer_id"]
            maly_sredni_dict["price"] = found_item["item_price"]
            maly_sredni_dict["name"] = found_item["item_name"]
            maly_sredni_dict["link"] = found_item["item_link"]
            maly_sredni_dict["delivery_price"] = found_item["delivery_price"]
            maly_sredni_dict["seller"] = found_item["seller"]

            sredni_dict[search_item_name] = maly_sredni_dict

            if seller_id not in sellers_found:

                sellers_found.add(seller_id)

                for other_inputed_item in keys.difference(excludes):
                    min_price, max_price, stan = get_price_range_and_state(
                        input_search_parameters[other_inputed_item]
                    )
                    returned_raw_data = fetch_module.get_seller_response(
                        RestApi,
                        other_inputed_item,
                        seller_id,
                        limit=1,
                        maximum_price=max_price,
                        minimum_price=min_price,
                        state=stan,
                    )
                    extracted_second_order_search_output = extractions.extract_valuable_info_from_raw_data(
                        returned_raw_data
                    )
                    try:

                        maly_dict = {}
                        maly_dict["id"] = extracted_second_order_search_output[0][
                            "offer_id"
                        ]
                        maly_dict["price"] = extracted_second_order_search_output[0][
                            "item_price"
                        ]
                        maly_dict["name"] = extracted_second_order_search_output[0][
                            "item_name"
                        ]
                        maly_dict["link"] = extracted_second_order_search_output[0][
                            "item_link"
                        ]
                        maly_dict[
                            "delivery_price"
                        ] = extracted_second_order_search_output[0]["delivery_price"]
                        maly_dict["seller"] = extracted_second_order_search_output[0][
                            "seller"
                        ]
                        sredni_dict[other_inputed_item] = maly_dict
                        DUZY_DICT[seller_id] = sredni_dict
                    except IndexError:
                        pass
                DUZY_DICT[seller_id] = sredni_dict
    return DUZY_DICT


def prepare_data_to_permutation(data, search_parameters):

    name_items_found_dict = {}
    for name in search_parameters:
        table_for_data = []
        for seller in data:
            for item in data[seller]:
                if item == name:
                    table_for_data.append(data[seller][name])
            name_items_found_dict[name] = table_for_data
    return name_items_found_dict


def permute_data(data):
    returned_list = []
    sorted_keys = sorted(data.keys())
    for element in itertools.product(*list(data[k] for k in sorted_keys)):
        returned_list.append(list(zip(sorted_keys, element)))
    return returned_list


def get_price(data):
    for set in data:
        seller_ids = []
        price_sum = 0.0
        iterator = 0
        delivery_prices = []
        max_delivery_price = 0.0
        duplicatess = []
        delivery_to_max = []
        was_checked = []
        previous_item_body = {}
        for item in set:
            item_body = item[1]

            seller = item_body['seller']
            price_sum += item_body['price']
            delivery_prices.append(item_body['delivery_price'])
            seller_ids.append(seller)
            for seller_id_index in range(len(seller_ids)-1):
                try:
                    if seller_ids[seller_id_index] == seller_ids[iterator]:
                        if(item_body['id'] not in was_checked):
                            duplicatess.append(item_body)
                            duplicatess.append(set[seller_id_index][1])
                            was_checked.append(item_body['id'])
                except IndexError:
                    pass
            iterator += 1
            if (iterator==1):
                was_checked.append(item_body['id'])

        if duplicatess:
            for duplicate in duplicatess:
                delivery_to_max.append(duplicate['delivery_price'])

            sum_of_delivery_price = sum(delivery_to_max)
            max_delivery_price = max(delivery_to_max)

            delivery_prices.append(-sum_of_delivery_price+max_delivery_price)

        price_sum += sum(delivery_prices)
        set.append(price_sum)

    return data


def get_cheapest_3_items(prepared_sets_of_articles):
    return (sorted(prepared_sets_of_articles, key=lambda x: x[-1]))[:3]


def print_links(data):
    print("WYNIK")
    for sets in data:
        print(80 * "-")
        cena_calkowita = sets[-1]
        for item in range(len(sets) - 1):
            item_body = sets[item][1]
            item_text = "\n\tszukane hasło: {}\n znaleziono: {} o id {} w cenie {}. \nlink {}".format(
                sets[item][0],
                item_body["name"],
                item_body["id"],
                item_body["price"],
                item_body["link"],
            )
            print(item_text)
        print("cena_calkowita = {}".format(round(cena_calkowita,2)))
    return


def get_data():
    multi_search_parameters = prepare_query()  # zapytanko
    # search params {'cos': [1, 2], 'cokolwiek': [3, 4]}
    first_order_data = {}

    # new_or_used=user_interaction.mozeUzywane()

    for item_name in multi_search_parameters:  # itemki
        print(item_name)
        haslo = item_name
        min_price, max_price, stan = get_price_range_and_state(
            multi_search_parameters[haslo]
        )  # cene

        returned_search_raw_data = fetch_module.get_response(
            RestApi, haslo, minimum_price=min_price, maximum_price=max_price, state=stan
        )  # zapytanie i odpowiedz raw

        list_of_items_returned_for_searched_item = extractions.extract_valuable_info_from_raw_data(
            returned_search_raw_data
        )

        first_order_data[
            item_name
        ] = list_of_items_returned_for_searched_item  # z pierwszego zapytania

    # # {szukany1: [znaleziony1, znaleziony2, ...], szukany2: [znaleziony1, znaleziony2, ...], ...}
    OUTPUT = look_for_other_items_in_sellers(
        first_order_data, multi_search_parameters
    )  ########
    OUTPUT = prepare_data_to_permutation(OUTPUT, multi_search_parameters)
    # utils.save_json(OUTPUT, 'prepared_data.json')
    OUTPUT = permute_data(OUTPUT)
    OUTPUT = get_price(OUTPUT)
    OUTPUT = get_cheapest_3_items(OUTPUT)
    print(print_links(OUTPUT))
    utils.save_json(OUTPUT)
    return OUTPUT


get_data()  # zaczynamy
print("\n\n---------------------------------------\n\t")
