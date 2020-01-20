def get_response(
    Object,
    phrase,
    limit=10,
    sorting="+price",
    minimum_price=10,
    maximum_price=25,
    state="11323_1",
    count=None):  # stan=11323_1 domyslnie nowy
    status_code, json_data = Object.resource_get(
        resource_name="/offers/listing",
        params={
            "phrase": phrase,
            "limit": limit,
            "sort": sorting,
            "price.from": int(minimum_price),
            "price.to": int(maximum_price),
            "sellingMode.format": "BUY_NOW",
            "parameter.11323": state,
        },
    )

    print("teraz", json_data)
    # for key in json_data.keys():
    #     print(key)

    for k, v in json_data.items():
        # print("k",k)
        # print("v",v)
        if k == "searchMeta" and v["totalCount"] == 0:
            print("i am in")
            if count==0:
                print(count)
                count=+1
                json_data = get_response(Object, phrase, minimum_price=10, maximum_price=25,state="11323_1",count=count)
                print("potem", json_data)
                break
            else:
                print("Zapytanie o {0} nie jest do zrealizowania, sprawdz poprawność parametrów a następnie wykonaj je jeszcze raz:)".format(phrase))
                return json_data

    return json_data  # status_code,


def get_seller_response(
    Object,
    phrase,
    seller_id,
    limit=10,
    sorting="+price",
    minimum_price=1,
    maximum_price=999999999,
    state="",
):
    status_code, json_data = Object.resource_get(
        resource_name="/offers/listing",
        params={
            "phrase": phrase,
            "limit": limit,
            "sort": sorting,
            "price.from": int(minimum_price),
            "price.to": int(maximum_price),
            "sellingMode.format": "BUY_NOW",
            "parametr.11323": state,
            "seller.id": seller_id,
        },
    )

    # print("teraz seller", json_data)
    # # for key in json_data.keys():
    # #     print(key)
    # for k, v in json_data.items():
    #     # print("k",k)
    #     # print("v",v)
    #     if k == 'searchMeta' and v['totalCount'] == 0:
    #         json_data = get_response(Object, phrase, minimum_price=10,
    #                                  maximum_price=25)
    #         break;
    #
    # print("potem seller ", json_data)

    return json_data
