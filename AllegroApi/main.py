from pyAllegro.api import AllegroRestApi
import json
from AllegroApi import extractions
from AllegroApi import checkSeller
from AllegroApi import fetch_module
from AllegroApi import utils
from AllegroApi import user_interaction

RestApi = AllegroRestApi()
# RestApi.load_token()

# Brakuje jeszcze:
# wyboru minimalnej ceny przedmiotow poszukiwanych
# parsowania listy przedmiotow i odpowiedniego zapisu odpowiedzi
# wybierania sprzedawcow z list i sprawdzania u nich ofert
# liczenia lacznej ceny i zwracania odpowiednio posortowanych odpowiedzi
# GUI/cokolwiek


def get_extracted_data(phrase, limit=20, sorting='+price', minumum_price=0, maximum_price=999999999):
    status_code, json_data = fetch_module.get_response(RestApi, phrase, limit, sorting, minumum_price, maximum_price)
    # save_json(json_data, filename='odpowiedz_surowa.json')
    item_list = extractions.extract_data(json_data)
    # utils.save_json(item_list)
    return item_list  # to zwraca listę artykulow pasujacych do wyszukiwanej frazy


def get_ex_seller_data(phase, sellerId): #funkcja ktora ma na celu sprawdzenie czy produkt o nazwie phase nie znajduje sie u innych sprzedawcow
    #jezeli sie znajduje to zwraca item i mozna tu np porownywac te produkty po cenie
    status_code, json_data = fetch_module.get_response_seller(RestApi, phase, sellerId)
    item_list_to_compare=extractions.extract_data_seller(json_data)
    # utils.save_json(item_list_to_compare)
    return item_list_to_compare  # ?


def write_responses_to_a_list(list_of_items_to_search): #dict
    responses_list = []
    # responses_dict = {}
    for item in list_of_items_to_search:  # dla kazdej frazy zwroc wyekstrachowana liste itemow na allegro
        # responses_dict[item] = get_extracted_data(item)
        responses_list.append(get_extracted_data(item))  # wez ten szajs i dodaj go do listy?
        # moze to nie bedzie zbyt szybkie, ale proste do napisania...
    return responses_list
    # return responses_dict


def run_this_program():
    # products_count = user_interaction.insert_count()
    # input_table = user_interaction.input_user(products_count)
    input_table = ['Kasza', 'Kurczaki']  # temporary
    first_order_responses = write_responses_to_a_list(input_table)  # DICT lista bezposrednich odpowiedzi na nasze zapytanie
    # print(type(first_order_responses))
    utils.save_json(first_order_responses)
    sellers = get_sellers(first_order_responses)
    utils.save_json(sellers, 'sellers.json')
    # dostajemy listę bezpośrednich odpowiedzi na nasze zapytanie.
    #
    # Teraz trzeba uzyskać listę sprzedawców dla każdego szukanego artykułu
    #
    #
    # seller_table = checkSeller.getSellers()  # tej tablicy
    # checkSeller.show()


def get_sellers(first_order_responses):
    sellers = {}
    print('first order response type : {}'.format(type(first_order_responses)))

    for item in first_order_responses:
        print(item)
        print('item type: {}'.format(type(item)))
        # print(first_order_responses[item])
        inner_dict = {}
        for offer in item:
            print('offer type: {}'.format(type(offer)))
            inner_dict[offer['seller']['id']] = offer['offer_id']
        sellers[item] = inner_dict
    return sellers
# run_this_program()

# for i in input_table:
#     get_ex_seller_data(i,'49703356') # tutaj jak wprowadzisz z palca seller.id to smiga, ale jak juz przekazuje z tej tablicy
#to wyszukuje tak jakby wgl nie bylo tego parametru podanego
#np. seller.id "49703356" i phase kokos i cokolwiek
#wynik zwraca duzo dla hasla kokos i czegos tam, a zapytanie wyciaga tylko dwa recordu w ktorych sie zgadza phase i seller.id


