menuList = []

def showBill():
    print("---- My Food----")
    tp = 0
    for number in range(len(menuList)):
        print(menuList[number])
        tp += menuList[number][1]
    print("Total Price: ", tp)

while True:
    menuName = str(input("Plese Enter Menu :"))
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price :"))
        menuList.append([menuName,menuPrice])

showBill()