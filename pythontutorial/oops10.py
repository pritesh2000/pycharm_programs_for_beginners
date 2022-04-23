# Public
# Protected
# Private

class Employee:
    no_of_leaves = 8
    _protec = 10
    __private = 122

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
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


mukesh = Employee.from_dash("Mukesh-3000-Panvala")
karan = Employee("Karan", 4000, "Programmer")
karan.change_leaves(23)
print(Employee.no_of_leaves)
print(mukesh.printdetails())
mukesh.printgood("mahesh")
print(karan._protec)                        # protected
print(karan._Employee__private)             # private is difficult
