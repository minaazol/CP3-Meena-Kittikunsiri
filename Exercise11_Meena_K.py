layer = int(input("No. of Christmas Tree Layer : "))
for x in range(layer):
  print(" "*(layer-x),"*"*((x+1)*2-1))
