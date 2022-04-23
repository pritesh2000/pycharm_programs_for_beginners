class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, apost):         # dunder method constructor because it starts with __
        self.name = aname
        self.salary = asalary
        self.post = apost

    def printdetails(self):
        return f"Name is {self.name} , Salary is {self.salary} and Post is {self.post}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):         # run when called but when str is absent though we call str, repr will return
        return f"Employee('{self.name}', {self.salary}, '{self.post}')"

    def __str__(self):          # default when both str and repr available
        return f"Name is {self.name} , Salary is {self.salary} and Post is {self.post}."


karan = Employee("Karan", 3000, "Programmer")
rohan = Employee("Rohan", 830, "Cleaner")
print(karan + rohan)
print(karan / rohan)
print(str(karan))
print(repr(karan))
