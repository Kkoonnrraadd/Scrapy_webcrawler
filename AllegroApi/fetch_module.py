import sys
global count
def get_response(
    Object,
    phrase,
    limit=10,
    sorting="+price",
    minimum_price=10,
    maximum_price=25,
    state="11323_1",
    count=0):  # stan=11323_1 domyslnie nowy
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

    for k, v in json_data.items():

        if k == "searchMeta" and v["totalCount"] == 0:

            if count==0:
                print(count)
                count+=1
                json_data = get_response(Object, phrase, minimum_price=10, maximum_price=25,state="11323_1",count=count)
                break

            elif count<4:

                print("Nie znaleźliśmy ofert dla frazy {0} \n".format(phrase))
                try:

                    phrase=input("Czy nie chciałbys zmienic frazy zamowienia ? Wykorzystane próby: {} / 3 \n".format(count))
                    count += 1
                    json_data = get_response(Object, phrase, minimum_price=10, maximum_price=25,state="11323_1",count=count)
                except TypeError:
                    sys.exit()
            else:
                print("Limit prób zostal wykorzystany. Spróbuj ponownie. ")
                sys.exit()

    return json_data


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

    return json_data
