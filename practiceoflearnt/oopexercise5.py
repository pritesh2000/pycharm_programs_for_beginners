class Vehicle:
    # class attributes
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


school_bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 190, 18)

print("Color:", Bus.color, "Vehicle name:", school_bus.name, "Maximum speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)
print("Color:", Car.color, "Vehicle name:", car.name, "Maximum speed:", car.max_speed, "Mileage:", car.mileage)
