import itertools

x = [["a", "b", "c"], ["d", "e"], ["f", "g"]]

# print(list(itertools.product(*x)))

y = []

z = {
    "x": {"a": {"da": 1}, "b": {"du": 2}},
    "y": {"c": {"dy": 3}, "d": {"de": 4}},
    "z": {"e": {"di": 5}, "f": {"do": 6}},
}
z = {
    "x": [{"da": 1}, {"du": 2}],
    "y": [{"dy": 3}, {"de": 4}],
    "z": [{"di": 5}, {"do": 6}],
}
print(list(itertools.product(*z)))


def dict_product(d):
    returned_list = []
    sorted_keys = sorted(d.keys())
    for element in itertools.product(*list(d[k] for k in sorted_keys)):
        returned_list.append(list(zip(sorted_keys, element)))
        # yield dict(zip(sorted_keys, element))
    return returned_list


ret = dict_product(z)
gowno = {
    "daktyle 1kg": [
        {
            "id": "7915202465",
            "price": 7.97,
            "name": "DAKTYLE SUSZONE 1kg - SUPER JAKO\u015a\u0106 PREMIUM DU\u017bE!",
            "link": "https://allegro.pl/oferta/daktyle-suszone-1kg---super-jakosc-premium-duze!-7915202465",
            "delivery_price": 6.99,
            "seller": "56303665",
        },
        {
            "id": "7598232126",
            "price": 7.99,
            "name": "Daktyle suszone bez pestek 1kg 1000g naturalne",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-1000g-naturalne-7598232126",
            "delivery_price": 6.7,
            "seller": "41189523",
        },
        {
            "id": "6333219461",
            "price": 8.19,
            "name": "DAKTYLE SUSZONE 1kg NATURALNE PYSZNE BEZ SO2",
            "link": "https://allegro.pl/oferta/daktyle-suszone-1kg-naturalne-pyszne-bez-so2-6333219461",
            "delivery_price": 6.69,
            "seller": "37365851",
        },
        {
            "id": "8740063369",
            "price": 8.2,
            "name": "Daktyle SUSZONE bez pestek 1kg NATURALNE S\u0141ODKIE",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-naturalne-slodkie-8740063369",
            "delivery_price": 7.99,
            "seller": "37029656",
        },
        {
            "id": "7662049481",
            "price": 8.2,
            "name": "Daktyle suszone bez pestek 1kg",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-7662049481",
            "delivery_price": 8.99,
            "seller": "24940007",
        },
        {
            "id": "7580867589",
            "price": 8.25,
            "name": "DAKTYLE suszone bez pestek 1kg NATURALNE s\u0142odkie",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-naturalne-slodkie-7580867589",
            "delivery_price": 5.9,
            "seller": "34836671",
        },
        {
            "id": "6737065698",
            "price": 8.29,
            "name": "DAKTYLE SUSZONE 1 kg NATURALNE PYSZNE",
            "link": "https://allegro.pl/oferta/daktyle-suszone-1-kg-naturalne-pyszne-6737065698",
            "delivery_price": 5.9,
            "seller": "38649086",
        },
        {
            "id": "6144752478",
            "price": 8.39,
            "name": "Daktyle SUSZONE bez pestek 1kg NATURALNE S\u0141ODKIE",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-naturalne-slodkie-6144752478",
            "delivery_price": 5.9,
            "seller": "3232608",
        },
        {
            "id": "7916626096",
            "price": 8.39,
            "name": "DAKTYLE SUSZONE 1 kg NATURALNE PYSZNE MrChef",
            "link": "https://allegro.pl/oferta/daktyle-suszone-1-kg-naturalne-pyszne-mrchef-7916626096",
            "delivery_price": 5.9,
            "seller": "50862095",
        },
        {
            "id": "7882121699",
            "price": 8.4,
            "name": "DAKTYLE SUSZONE 1 kg NATURALNE \u015aWIE\u017bE SUPER JAKO\u015a\u0106",
            "link": "https://allegro.pl/oferta/daktyle-suszone-1-kg-naturalne-swieze-super-jakosc-7882121699",
            "delivery_price": 6.7,
            "seller": "46113904",
        },
        {
            "id": "6334949623",
            "price": 8.49,
            "name": "DAKTYLE SUSZONE 1kg BEZ PESTEK PREMIUM",
            "link": "https://allegro.pl/oferta/daktyle-suszone-1kg-bez-pestek-premium-6334949623",
            "delivery_price": 6.69,
            "seller": "39694449",
        },
        {
            "id": "7569468429",
            "price": 8.5,
            "name": "DAKTYLE Suszone Bez Pestek 1kg, PYSZNE - MIGOgroup",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg,-pyszne---migogroup-7569468429",
            "delivery_price": 8.0,
            "seller": "37441213",
        },
        {
            "id": "7487937321",
            "price": 8.53,
            "name": "DAKTYLE SUSZONE BEZ PESTEK 1Kg / Swojska Piwniczka",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-/-swojska-piwniczka-7487937321",
            "delivery_price": 8.99,
            "seller": "23642818",
        },
        {
            "id": "8097679859",
            "price": 8.5,
            "name": "DAKTYLE Suszone Bez pestek 1kg, PYSZNE - MIGOgroup",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg,-pyszne---migogroup-8097679859",
            "delivery_price": 8.0,
            "seller": "44227315",
        },
        {
            "id": "8241451467",
            "price": 10.99,
            "name": "DAKTYLE SUSZONE BEZ PESTEK 1kg NATURALNE S\u0141ODKIE",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-1kg-naturalne-slodkie-8241451467",
            "delivery_price": 8.99,
            "seller": "37530514",
        },
        {
            "id": "6333914353",
            "price": 8.9,
            "name": "DAKTYLE suszone bez pestek najwy\u017csza jako\u015b\u0107 1kg",
            "link": "https://allegro.pl/oferta/daktyle-suszone-bez-pestek-najwyzsza-jakosc-1kg-6333914353",
            "delivery_price": 6.5,
            "seller": "41163209",
        },
    ],
    "Orzechy arachidowe 1kg": [
        {
            "id": "7586286090",
            "price": 11.59,
            "name": "Orzechy arachidowe orzeszki ziemne bez sol 1kg",
            "link": "https://allegro.pl/oferta/orzechy-arachidowe-orzeszki-ziemne-bez-sol-1kg-7586286090",
            "delivery_price": 6.7,
            "seller": "41189523",
        },
        {
            "id": "7338459630",
            "price": 11.39,
            "name": "ORZECHY ZIEMNE 1KG ARACHIDOWE PRA\u017bONE BEZ SOLI",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-1kg-arachidowe-prazone-bez-soli-7338459630",
            "delivery_price": 6.69,
            "seller": "37365851",
        },
        {
            "id": "8379001882",
            "price": 10.5,
            "name": "Orzechy ARACHIDOWE BEZ SOLI 1kg NATURALNE 1000g",
            "link": "https://allegro.pl/oferta/orzechy-arachidowe-bez-soli-1kg-naturalne-1000g-8379001882",
            "delivery_price": 5.9,
            "seller": "34836671",
        },
        {
            "id": "6753628303",
            "price": 11.99,
            "name": "ORZECHY ZIEMNE ARACHIDOWE PRA\u017bONE 1kg POSYPKA!",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-1kg-posypka!-6753628303",
            "delivery_price": 5.9,
            "seller": "38649086",
        },
        {
            "id": "4971049580",
            "price": 11.69,
            "name": "Orzechy ziemne ARACHIDOWE pra\u017cone 1kg NATURALNE",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-1kg-naturalne-4971049580",
            "delivery_price": 5.9,
            "seller": "3232608",
        },
        {
            "id": "7916631140",
            "price": 11.99,
            "name": "ORZECHY ZIEMNE POSYPKA 1kg ARACHIDOWE MrChef",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-posypka-1kg-arachidowe-mrchef-7916631140",
            "delivery_price": 5.9,
            "seller": "50862095",
        },
        {
            "id": "7400440222",
            "price": 10.57,
            "name": "ORZECHY ZIEMNE 1KG ARACHIDOWE PRA\u017bONE BEZ SOLI",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-1kg-arachidowe-prazone-bez-soli-7400440222",
            "delivery_price": 6.69,
            "seller": "39694449",
        },
        {
            "id": "7600774235",
            "price": 10.6,
            "name": "Orzechy ziemne ARACHIDOWE pra\u017cone 1kg - MIGOgroup",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-1kg---migogroup-7600774235",
            "delivery_price": 8.0,
            "seller": "37441213",
        },
        {
            "id": "7338045229",
            "price": 10.79,
            "name": "Orzechy ziemne ARACHIDOWE pra\u017cone 1kg bez soli / S",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-1kg-bez-soli-/-s-7338045229",
            "delivery_price": 8.99,
            "seller": "23642818",
        },
        {
            "id": "7600905353",
            "price": 10.9,
            "name": "Orzechy ZIEMNE ARACHIDOWE pra\u017cone 1kg - MIGOgroup",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-1kg---migogroup-7600905353",
            "delivery_price": 8.0,
            "seller": "44227315",
        },
        {
            "id": "8456699055",
            "price": 11.97,
            "name": "ORZESZKI ZIEMNE ORZECHY ARACHIDOWE PREMIUM 1kg",
            "link": "https://allegro.pl/oferta/orzeszki-ziemne-orzechy-arachidowe-premium-1kg-8456699055",
            "delivery_price": 6.7,
            "seller": "63234210",
        },
        {
            "id": "8251595175",
            "price": 12.19,
            "name": "ORZECHY ZIEMNE ARACHIDOWE PRA\u017bONE 1kg NATURALNE",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-1kg-naturalne-8251595175",
            "delivery_price": 8.99,
            "seller": "37530514",
        },
        {
            "id": "6306561803",
            "price": 12.9,
            "name": "ORZECHY ZIEMNE ARACHIDOWE pra\u017cone bez soli 1 kg",
            "link": "https://allegro.pl/oferta/orzechy-ziemne-arachidowe-prazone-bez-soli-1-kg-6306561803",
            "delivery_price": 6.5,
            "seller": "41163209",
        },
    ],
    "g\u00f3wno w papierku": [],
}
gowna_dwa = dict_product(gowno)

print(gowna_dwa)
print(ret)


for sett in ret:
    for item in sett:
        # print(item[1])
        pass
