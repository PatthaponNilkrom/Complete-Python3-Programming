menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    print("Total Price: ",sum(priceList))

while True:
    menuName = str(input("Plese Enter Menu :"))
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()