#11/12/2025
#Inheratence OOP example


class vehicle:
    def __init__(self, name, topSpeed, maxPassengers):
        self.topSpeed = topSpeed
        self.maxPassengers = maxPassengers
        self.name = name
    def printInfo(self):
        print(f"{self.name} statistics")
        print(f"Top speed --> {self.topSpeed}")
        print(f"Max passengers -->{self.maxPassengers}")

class Truck(vehicle):
    def __init__(self, name, topSpeed, maxPssengers, CarryCapacity):
        super().__init__(name, topSpeed, maxPssengers)
        self.CarryCapacity = CarryCapacity
    def CarryCapacityInfo(self):
        self.printInfo()
        print(f"Carry capacity --> {self.CarryCapacity}")

class Car(vehicle):
    def __init__(self, name, topSpeed, maxPssengers, economy):
        super().__init__(name, topSpeed, maxPssengers)
        self.economy = economy
    def Eco(self):
        self.printInfo()
        print(f"this car has {self.economy} economic performance")
        
class Plane(vehicle):
    def __init__(self, name, topSpeed, maxPssengers, MaxRange):
        super().__init__(name, topSpeed, maxPssengers)
        self.MaxRange = MaxRange
    def MaxRangeInfo(self):
        self.printInfo()
        print(f"Maximum range --> {self.MaxRange}")


VolvoFL = Truck("Volvo FL Electric",90, 2, "18.6 tons")
Lambo = Car("Lambo",220, 2, "poor")
plane = Plane("plen",350, 200, 3600)

VolvoFL.CarryCapacityInfo()
print("")
Lambo.Eco()
print("")
plane.MaxRangeInfo()