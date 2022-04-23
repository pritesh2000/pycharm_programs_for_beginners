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

    @classmethod
    def from_coma(cls, string):
        return cls(*string.split(","))
        # rama = string.split(",")
        # return cls(rama[0], rama[1], rama[2])

    @staticmethod
    def printgood(string):
        print("This is good " + string)


rohan = Employee("Rohan", 5000, "Student")
mohan = Employee("Mohan", 4000, "Instructor")
karan = Employee.from_coma("Karan,3000,Teacher")
print(rohan.salary)
rohan.change_leaves(34)
print(Employee.no_of_leaves)
print(karan.post)
karan.printgood("Pritesh")
