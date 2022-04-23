def outerfunc(a, b):
    square = a ** 2

    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5


print(outerfunc(5, 4))
