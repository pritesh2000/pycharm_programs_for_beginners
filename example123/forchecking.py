# Fibonacci

A = int(input("Enter the number: "))


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(tuple(fibonacci(A)))

# Factorial

A = int(input("Enter the number: "))


def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
        yield fact


print(tuple(factorial(A)))
