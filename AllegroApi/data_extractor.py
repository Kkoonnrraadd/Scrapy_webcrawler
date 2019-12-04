from AllegroApi import checkSeller

def extract_data(json_data):
    items = []
    for typ_oferty in json_data['items']:
        # print(typ_oferty)
        for oferty in json_data['items'][typ_oferty]:
            # print(oferty)
            offer_id = oferty['id']
            name = oferty['name']
            # print(name)
            seller = oferty['seller']

            id_seller=oferty['seller']['id']
            checkSeller.addSeller(id_seller)
            #+url do wyswietlania w GUI
            # url_img=typy['images']['url']
            if (oferty['delivery']['availableForFree'] is False):
                delivery_price = oferty['delivery']['lowestPrice']['amount']
            else:
                # print(oferty['delivery']['availableForFree'])
                delivery_price = 0
            item_price = oferty['sellingMode']['price']['amount']
            stock = oferty['stock']['available']
            category_id = oferty['category']['id']

            oferta = {'offer_id': offer_id, 'item_name': name, 'seller': seller, 'delivery_price': delivery_price,
                      'item_price': item_price, 'stock': stock, 'category_id': category_id}
            items.append(oferta)
    return items


def extract_data_seller(data): # to samo co wyzej, bez sensu
    # print(data)
    items=[]
    for typ_oferty in data['items']:

        for oferta in data['items'][typ_oferty]:

            offer_id = oferta['id']
            name = oferta['name']
            seller = oferta['seller']
            #url_img=typy['images']['url']
            if (oferta['delivery']['availableForFree'] is False):
                delivery_price = oferta['delivery']['lowestPrice']['amount']
            else:
                # print(oferta['delivery']['availableForFree'])
                delivery_price = 0
            item_price = oferta['sellingMode']['price']['amount']
            stock = oferta['stock']['available']
            category_id = oferta['category']['id']

            oferta = {'offer_id': offer_id, 'item_name': name, 'seller': seller, 'delivery_price': delivery_price,
                      'item_price': item_price, 'stock': stock, 'category_id': category_id}
            # print(oferta)
            items.append(oferta)
        return items


