def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("login Error!!")
        return login()
def showMenu():
    print("----My shop----")
    print("1. Vat Calculate")
    print("2. Price Calculate")
    print("---------------")
    return menuSelect()
def menuSelect():
    userSelect = int(input("Choose number >> : "))
    if userSelect == 1:
        print(vatCalculate(float(input("Price is : "))))
    elif userSelect == 2:
        print(priceCalculate())
    else:
        print("Please enter the menu again : ")
        return manuSelect()
def vatCalculate(price):
    vat = 7
    result = price + (price*vat/100)
    return "Total Price is : "+str(result)
def priceCalculate():
    price1 = int(input("First product   >> : "))
    price2 = int(input("Second product  >> : "))
    return vatCalculate(price1+price2)

login()
