def extract_data(json_data):
    items = []
    for typ_oferty in json_data['items']:
        # print(typ_oferty)
        for oferty in json_data['items'][typ_oferty]:
            # print(oferty)
            offer_id = oferty['id']
            name = oferty['name']
            seller = oferty['seller']

            if (oferty['delivery']['availableForFree'] is False):
                delivery_price = oferty['delivery']['lowestPrice']['amount']
            else:
                print(oferty['delivery']['availableForFree'])
                delivery_price = 0
            item_price = oferty['sellingMode']['price']['amount']
            stock = oferty['stock']['available']
            category_id = oferty['category']['id']

            oferta = {'offer_id': offer_id, 'item_name': name, 'seller': seller, 'delivery_price': delivery_price,
                      'item_price': item_price, 'stock': stock, 'category_id': category_id}
            items.append(oferta)
    return items