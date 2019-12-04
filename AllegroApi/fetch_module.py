def get_response(Object, phrase, limit=10, sorting='+price', minimum_price=0, maximum_price=999999999):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'limit': limit,
                'sort': sorting,
                'sellingMode.price.amount.gte': int(minimum_price),  # nie dziala jeszcze
                'sellingMode.price.amount.lte': int(maximum_price),  # nie dziala jeszcze
                'sellingMode.format': "BUY_NOW"}
    )
    return status_code, json_data


def get_response_seller(Object, phrase, sellerId, limit=5, searchMode="REGULAR" ):
    status_code, json_data = Object.resource_get(
        resource_name='/offers/listing',
        params={'phrase': phrase,
                'seller.id': sellerId,
                'limit': limit,
                'searchMode': searchMode
                    }
    )
    return status_code, json_data