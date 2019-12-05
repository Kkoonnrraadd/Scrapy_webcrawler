def get_response(Object, phrase, limit=10, sorting='+price', minimum_price=0, maximum_price=999999999):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'limit': limit,
                'sort': sorting,
                'price.from': int(minimum_price),
                'price.to': int(maximum_price),
                'sellingMode.format': "BUY_NOW"}
    )
    return json_data  #status_code,


def get_seller_response(Object, phrase, seller_id, limit=10, sorting='+price', minimum_price=0, maximum_price=999999999):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'limit': limit,
                'sort': sorting,
                'price.from': int(minimum_price),
                'price.to': int(maximum_price),
                'sellingMode.format': "BUY_NOW",
                'seller.id': seller_id}
    )
    return json_data  #status_code,

def get_response_seller(Object, phrase, sellerId, limit=1, searchMode="REGULAR",
                        sorting='+price', minimum_price=0, maximum_price=999999999):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'seller.id': sellerId,
                'sort': sorting,
                'price.from': minimum_price,
                'price.to': maximum_price,
                'limit': limit,
                'searchMode': searchMode
                    }
    )
    return json_data  # status_code

# def get_response_from_seller(Object, phrase, seller_id, limit=1, searchMode="REGULAR", sorting='+price',
#                              minimum_price=0, maximum_price=999999999):
#     status_code, json_data = Object.resource_get(
#         resource_name='/sale/offers',
#         params={'name': phrase,
#                 'phrase': phrase,
#                 'sellingMode.price.amount.gte': minimum_price,
#                 'sellingMode.price.amount.lte': maximum_price,
#                 'limit': limit,
#                 'sort': sorting #,
#                 # 'price.from': minimum_price,
#                 # 'price.to': maximum_price
#                 }
#     )
