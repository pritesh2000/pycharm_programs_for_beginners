# Fibonacci series
a, b = 0, 1
n = int(input("Enter number:"))
print("Fibonacci Sequence:")
while n != 0:
    print(a, end="  ")
    a, b = b, a + b
    n -= 1
