class Employee:
    no_of_leaves = 8
    pass


mohan = Employee()
rohan = Employee()

mohan.name = "Mohan"
mohan.salary = 4000
mohan.post = "Instructor"

rohan.name = "Rohan"
rohan.salary = 5000
rohan.post = "Student"

print(rohan.name, mohan.salary, mohan.no_of_leaves, Employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 9
print(rohan.__dict__)
Employee.no_of_leaves = 9
print(Employee.no_of_leaves)
print(Employee.__dict__)