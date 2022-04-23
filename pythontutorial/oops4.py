class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, apost):
        self.name = aname
        self.salary = asalary
        self.post = apost

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and Post is {self.post}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


rohan = Employee("Rohan", 4000, "Student")
mohan = Employee("Mohan", 5000, "Instructor")

Employee.no_of_leaves = 87
mohan.change_leaves(45)             # must for change
print(mohan.printdetails())
print(rohan.no_of_leaves)
