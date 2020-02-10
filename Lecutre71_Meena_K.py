menuList = []
priceList = []

def bill():
  print("------My Shop------")
  for i in range(len(priceList)):
    print(menuList[i], priceList[i])
    print("Total :",sum(priceList))

while True:
  menu = input("Please enter menu : ")
  if menu.lower() == 'exit':
    break
  else: 
    price = int(input("Please enter price : "))

  menuList.append(menu)
  priceList.append(price)

bill()
