
s = int(input("Enter number:"))
n = s
a = 1
if n < 0:
    print("Factorial does not exist in negative number.")
elif n == 0:
    print("Factorial of 0 is 1.")
else:
    while n >= 1:
        a = a * n
        n -= 1
    print(f"Factorial of {s} is {a}")

