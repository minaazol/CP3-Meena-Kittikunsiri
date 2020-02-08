price = int(input("Price : "))

def totalPrice(x):
  result = x+(x*7/100)
  return result

print("Total price is : "+str(totalPrice(price)))
