class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}."

    @property                                     # property is decorator so we do not need to call function
    def email(self):                              # setters is function
        if self.fname is None or self.lname is None:
            return "Email is not set. \nPlease set it using setter."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter                                 # this is particular setter which is not callable
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


karan = Employee("Karan", "Vala")
rohan = Employee("Rohan", "Das")

print(karan.explain())
print(karan.email)

karan.fname = "Kiran"
print(karan.email)

karan.email = "this.that@gmail.com"
print(karan.email)

del karan.email
print(karan.email)

karan.email = "karan.vala@gmail.com"
print(karan.email)
