# from AllegroApi import checkSeller
from AllegroApi import utils


def extract_valuable_info_from_raw_data(json_data):
    returned_items_list = []

    for typ_oferty in json_data["items"]:

        for oferty in json_data["items"][typ_oferty]:
            offer_id = oferty["id"]
            name = oferty["name"]

            id_seller = oferty["seller"]["id"]
            if oferty["delivery"]["availableForFree"] is False:
                delivery_price = oferty["delivery"]["lowestPrice"]["amount"]
            else:
                delivery_price = 0
            item_price = oferty["sellingMode"]["price"]["amount"]
            stock = oferty["stock"]["available"]
            category_id = oferty["category"]["id"]

            oferta = {
                "offer_id": offer_id,
                "item_name": name,
                "seller": id_seller,
                "delivery_price": float(delivery_price),
                "item_price": float(item_price),
                "item_link": utils.generete_link(name, offer_id),
            }
            returned_items_list.append(oferta)

    return returned_items_list


def extract_data_seller(data):
    items = []
    for typ_oferty in data["items"]:

        for oferta in data["items"][typ_oferty]:

            offer_id = oferta["id"]
            name = oferta["name"]
            seller = oferta["seller"]
            # url_img=typy['images']['url']
            if oferta["delivery"]["availableForFree"] is False:
                delivery_price = oferta["delivery"]["lowestPrice"]["amount"]
            else:
                delivery_price = 0
            item_price = oferta["sellingMode"]["price"]["amount"]
            stock = oferta["stock"]["available"]
            category_id = oferta["category"]["id"]

            oferta = {
                "offer_id": offer_id,
                "item_name": name,
                "seller": seller,
                "delivery_price": float(delivery_price),
                "item_price": float(item_price),
                "item_link": utils.generete_link(name, offer_id),
            }
            items.append(oferta)
        return items


def get_price_only(list_of_items):
    list_of_prices = []
    for item in list_of_items:
        list_of_prices.append(float(item["item_price"]))
    list_of_prices.sort()
    return list_of_prices
