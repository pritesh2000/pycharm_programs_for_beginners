class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


school_bus = Bus("School Volvo", 14, 50)
print(isinstance(school_bus, Vehicle))
