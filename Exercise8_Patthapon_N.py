u=input("Username: ")
p=input("Password: ")
cc=12
ec=10
if u== "admin" and p== "1234":
    print("login complete")
    print("Welcome to iShop")
    print("1. Cocacola:",cc," Baht")
    print("2. est cola:",ec," Baht")
    us=int(input("=>"))
    if us== 1:
        n = float(input('Number of products to buy: '))
        result = n*cc
        print("Price",result)
    elif us==2:
        n = float(input('Number of products to buy: '))
        result = n * ec
        print("Price",result)
else:
    print("login failed")
