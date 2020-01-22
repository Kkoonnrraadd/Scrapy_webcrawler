import json
import unidecode


def save_json(json_data, filename="zapytanie.json"):
    with open(filename, "w") as zapytanie:
        json.dump(json_data, zapytanie)


def generete_link(item_name, item_id):

    item_name = unidecode.unidecode(item_name).lower().replace(" ", "-").replace('.', '-')
    for ch in ['@', '~', '#', '$', '%', '^', '&', '*', '|', '+', '}', '{', '=']:
        item_name = item_name.replace(ch, '')
    preamble = "https://allegro.pl/oferta/"
    link = "{}{}-{}".format(preamble, item_name, item_id)
    return link
