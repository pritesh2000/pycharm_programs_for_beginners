# function runs only when it is called

def f():
    print("Hello world")


f()


def f(yep):
    print(yep + " hahaha")


f("go")
f("mac")
f("fine")


def f(next, string):
    print(next + " " + string)


f("max", "difference")


def f(*asp):
    print("The youngest child is " + asp[2])


f("meena", "sopa", "vicky")


def f(x):
    return 5 * x


print(f(3))
print(f(4))
print(f(9))

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


import random
i = random.randrange(1, 3)
print(random.randrange(1, 10))
print(random.random())
print(i)
if i >= 2:
    print("show")
