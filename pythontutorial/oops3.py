class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, apost):
        self.name = aname
        self.salary = asalary
        self.post = apost

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and Post is {self.post}"


mohan = Employee("Mohan", 4000, "Instructor")
# rohan = Employee()

# mohan.name = "Mohan"
# mohan.salary = 4000
# mohan.post = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 5000
# rohan.post = "Student"

# print(rohan.printdetails())
print(mohan.printdetails())
