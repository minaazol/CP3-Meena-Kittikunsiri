User = input("username: ")
Password = input("password: ")
if User == "client" and Password == "1234":
    print("Login Success")
    print("-----WELCOME TO OUR INSTITUTION-----")
    print("1. DESIGN THINKING COURSE    : 20000 THB")
    print("2. PROJECT MANAGEMENT COURSE : 30000 THB")
    print("3. PYTHON PROGRAMMING COURSE : 25000 THB")
    Selection = int(input("Course no.  : "))
    Head = int(input("Number of people : "))
    if Selection == 1:
        price = 20000 * Head
        vat = 7
        print("Total price is : ",price + (price * vat / 100))
    elif Selection == 2:
        price = 30000 * Head
        vat = 7
        print("Total price is : ",price + (price * vat / 100))
    elif Selection == 3:
        price = 25000 * Head
        vat = 7
        print("Total price is : ",price + (price * vat / 100))
    
    print("Program Closed")
else:
    print("Error Login")
