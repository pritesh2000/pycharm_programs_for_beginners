class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country

first_item = Jets("F16", "USA")
a = first_item.name
b = first_item.origin
print(a, b)