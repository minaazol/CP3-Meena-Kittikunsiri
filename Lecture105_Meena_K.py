class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAir(self):
        print("Turn On : Air")

class Car(Vehicle):
  pass

class Pickup(Vehicle):
    def sayhello(self):
        print("Hello")

class Van(Vehicle):
  pass

class Estatecar(Vehicle):
  pass

car1 = Car()
car1.turnOnAir()

Pickup1 = Pickup()
Pickup1.turnOnAir()
Pickup1.sayhello()

Van1 = Van()
Van1.turnOnAir()

estatecar1 = Estatecar()
estatecar1.turnOnAir()
