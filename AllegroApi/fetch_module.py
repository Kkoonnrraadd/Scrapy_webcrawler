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
    return json_data  # status_code,


def get_seller_response(Object, phrase, seller_id, limit=10, sorting='+price', minimum_price=0,
                        maximum_price=999999999):
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
    return json_data