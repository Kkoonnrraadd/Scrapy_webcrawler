def get_response(Object, phrase, limit=10, sorting='+price', minimum_price=0, maximum_price=999999999):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'limit': limit,
                'sort': sorting,
                'price.from': int(minimum_price),  # nie dziala jeszcze
                'price.to': int(maximum_price),  # nie dziala jeszcze
                'sellingMode.format': "BUY_NOW"}
    )
    return json_data  #status_code,


def get_response_seller(Object, phrase, sellerId, limit=5, searchMode="REGULAR" ):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'seller.id': sellerId,
                'limit': limit,
                'searchMode': searchMode
                    }
    )
    return json_data  # status_code