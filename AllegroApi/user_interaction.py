def insert_count(): #user podaje liczbe produktow
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


def input_user(products_count): #user wprowadza produkty
    input_table = []
    for i in range(products_count):
        k = input("Enter the name: ")
        input_table.append(k)
    return input_table