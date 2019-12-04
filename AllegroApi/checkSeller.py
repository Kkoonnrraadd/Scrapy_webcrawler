import json
sellers=[]

def getSellers():
    return sellers

def addSeller(data):

    str_data = json.dumps(data)
    print("SELLER: "+str_data)
    sellers.append(str_data)

def show():
    for i in sellers:
        print(i)