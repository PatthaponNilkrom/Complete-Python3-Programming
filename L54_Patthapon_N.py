def login():
    u = input("Username: ")
    p = input("Password: ")
    if u == "admin" and p == "1234":
        print("login complete")
        return showMenu()
    else:
        print("login failed")
        return login()
def showMenu():
    print("Welcome to iShop")
    print("1. Cocacola:", 12, " Baht")
    print("2. est cola:", 10, " Baht")
    print("3. logout")
    return menu()
def menu():
    us = int(input("=>"))
    if us==1:
        n = float(input('Number of products to buy: '))
        re = n*12
    elif us==2:
        n = float(input('Number of products to buy: '))
        re = n * 10
    elif us==3:
        return exit()
    return vatCal(re)
def vatCal(tp):
    v = float(input('Vat(%): '))
    result = tp + (tp * v / 100)
    return priceCal(result)
def priceCal(price):
    print('Price: ',price)
    return showMenu()
print(login())