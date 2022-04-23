# multiple inheritance
class Employee:
    no_of_leaves = 8
    var = 8

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


class Player:
    no_of_games = 4
    var = 9

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name} and Game is {self.game}."


class CoolProgrammer(Employee, Player):

    language = "C++"

    def printlanguage(self):
        print(self.language)


rohan = Employee("Rohan", 5000, "Student")
mohan = Employee("Mohan", 4000, "Instructor")

shubham = Player("Shubham", ["Cricket"])

karan = CoolProgrammer("Karan", 8000, "CoolProgrammer")

et = karan.printdetails()
karan.printlanguage()
print(et)
print(karan.var)




