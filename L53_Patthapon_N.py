def vatCal(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result
print(vatCal(float(input("Price: "))))