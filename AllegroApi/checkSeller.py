import json

sellers = []

def getSellers():
    return sellers

def addSeller(data): #pobieram id i zamieniam na string

    str_data = json.dumps(data)
    print("SELLER: "+str_data)
    sellers.append(str_data)

def show():
    for i in sellers:
        print(i)

def addOfferid(data):
    str_data = json.dumps(data)
    #print("OFFER_ID: " + str_data)
    sellers.append(str_data)
