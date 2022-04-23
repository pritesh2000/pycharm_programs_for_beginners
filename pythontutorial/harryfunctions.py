a = 9
b = 8
c = sum((a, b))  # built in functions
print(c)


def func1(a, b):
    print("Hello you are in function ", a+b)
func1(5, 7)


def func2(a, b):
    """This is the function which calculate average of two numbers"""
    average = (a+b)/2
    print(average)
    return average

v = func2(5, 7)
print(v)
print(func2.__doc__)
