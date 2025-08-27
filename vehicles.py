#Activity 2
class Car:
    def move(self):
        print("Car is driving 🚗")

class Plane:
    def move(self):
        print("Plane is flying ✈️")

class Boat:
    def move(self):
        print("Boat is sailing ⛵")

class Bike:
    def move(self):
        print("Bike is pedaling 🚴")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()
