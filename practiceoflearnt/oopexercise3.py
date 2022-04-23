class Vehicle:

    def __init__(self, name, mileage, max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed


# modelX = Vehicle("Hero", 23, 240)
# print(modelX.name, modelX.mileage, modelX.max_speed)

class Bus(Vehicle):
    pass


school_bus = Bus("Volvo", 24, 180)
print("Vehicle name:", school_bus.name, "\nMaximum speed:", school_bus.max_speed, "\nMileage:", school_bus.mileage)
