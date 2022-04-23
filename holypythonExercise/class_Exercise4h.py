class Myfunc:
    def power(x, y):
        return x ** y

    def __str__(self):
        return "Myfunc is a class which is capable of mathematical operations like raising a number to a power with " \
               "power function."


ans1 = Myfunc.power(5, 6)
ans2 = Myfunc()

print(ans1)
print(ans2)
