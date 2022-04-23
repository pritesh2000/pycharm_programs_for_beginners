# Classes - Template
# Object - Instance Of the Class
# DRY - Do not Repeat Yourself

# get_no_of_films()

class Student:
    # def __init__(self, names, stan):
    #     self.fname = names
    #     self.cla = stan
    pass

pritesh = Student()
mukesh = Student()

pritesh.name = "Pritesh"
pritesh.std = 12
pritesh.section = "A"
mukesh.std = 9
mukesh.subjects = ["Gujarati", "Hindi"]

print(pritesh.section, mukesh.subjects)
print(pritesh, mukesh)
