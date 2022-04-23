class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, apost):
        self.name = aname
        self.salary = asalary
        self.post = apost

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and Post is {self.post}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # para = string.split("-")
        # return cls(para[0], para[1], para[2])
        return cls(*string.split("-"))


mohan = Employee("Mohan", 4000, "Instructor")
rohan = Employee("Rohan", 5000, "Student")
karan = Employee.from_dash("Karan-3000-Teacher")

rohan.change_leaves(23)
print(Employee.no_of_leaves)
print(karan.salary)
print(karan.no_of_leaves)
