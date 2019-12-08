def insert_count():  # user podaje liczbe produktow
    try:
        product_count = int(input("Wpisz ilość produktów:\n"))
        if product_count < 0 or product_count > 5:
            print("Podano nieprawidłową wartość")
            return insert_count()
        else:
            return product_count
    except ValueError:
        print("Podano nieprawidłową wartość")
        return insert_count()


def input_user():  # user wprowadza produkty

    name = input("Enter the name: ")
    min_price, max_price = minImax()
    input_us={ name : [min_price,max_price] }
    return input_us

def minImax():
    try:
        pricemin = int(input('Podaj cenę minimalną:'))
        pricemax = int(input('Podaj cenę minimalną:'))
        if pricemin < 0:
            print('Podano liczbę mniejszą od 0.')
            return minImax()
        if not pricemin <= pricemax:
                print('Cena maksymalna jest mniejsza od minimalnej!')
                return minImax()

        return pricemin,pricemax
    except ValueError:
        print('Podano nieprawidłową wartość.')
        return minImax()
