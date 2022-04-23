# single inheritance
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

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56

    def __init__(self, aname, asalary, apost, alanguage):
        self.name = aname
        self.salary = asalary
        self.post = apost
        self.languages = alanguage

    def printprog(self):
        return f"The Programmer's name is {self.name}, Salary is {self.salary} and Post is {self.post}." \
               f"Learnt languages are {self.languages}"


rohan = Employee("Rohan", 5000, "Student")
mohan = Employee("Mohan", 4000, "Instructor")

karan = Programmer("Karan", 7000, "Programmer", ["python"])
shubham = Programmer("Shubham", 8000, "Programmer", ["python, c++"])

print(shubham.printprog())
print(karan.no_of_holiday)
