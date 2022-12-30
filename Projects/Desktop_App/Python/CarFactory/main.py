class Engine():
    def __init__(self):
        print("I am Engine object")

    def __str__(self):
        return "I am engine"

class Chassis():
    def __init__(self):
        print("I am Chassis object")

    def __str__(self):
        return "I am chassis"

class Tyre():
    def __init__(self):
        print("I am Tyre object")

    def __str__(self):
        return "I am tyre"
    
class Seat():
    def __init__(self):
        print("I am Seat object")

    def __str__(self):
        return "I am seat"

class DashBoard():
    def __init__(self):
        print("I am DashBoard object")
    
    def __str__(self):
        return "I am dashboard"

class AirBag():
    def __init__(self):
        print("I am AirBag object")

    def __str__(self):
        return "I am airbag"

class AirConditioning():
    def __init__(self):
        print("I am AirConditioning object")

    def __str__(self):
        return "I am airconditioning"

class Brake():
    def __init__(self):
        print("I am Brake object")

    def __str__(self):
        return "I am brake"

class PowerTrain():
    def __init__(self):
        print("I am PowerTrain object")

    def __str__(self):
        return "I am powertrain"

class Body():
    def __init__(self):
        print("I am Body object")

    def __str__(self):
        return "I am body"

class Vehicle:
    machineType = ""    #class attributes, always initialize them use them when you want them same for all objects
    engine = Engine()
    chassis = Chassis()
    seats =[]               #Seat()
    dashboard = DashBoard()
    ac = AirConditioning()
    brakes = []             #Brake()
    powerTrain = PowerTrain()
    body = Body()
    def __init__(self):
        pass
    def getEngine(self):
        return self.engine

    def getChassis(self):
        return self.chassis    
    
    def getDashboard(self):
        return self.dashboard

    def getAirConditioning(self):
        return self.ac

    def getPowerTrain(self):
        return self.powerTrain
    
    def getBody(self):
        return self.powerTrain


    def __str__(self):
        return "Autombile have Engine, Brakes, PowerTrain, Seats, DashBoard, AC, AirBags" 


class Car:
    brand = ""
    group = ""
    operationType = "Land"

    tyres =[]               #Tyre()
    airbags =[]             #AirBags()

    def __init__(self, name, group):
        # self.machineType = "Motor Car"
        self.brand = name
        self.group = group

    def __str__(self):
        return f"This is {self.group} Group's {self.brand} brand car "


kiaCar = Car("Kia", "Hyundai")
print(kiaCar)

jaguarCar = Car("Jaguar", "Tata")
print(jaguarCar)

# print(isinstance(kiaCar, Vehicle))
