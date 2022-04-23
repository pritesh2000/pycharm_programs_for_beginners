# Reverse number
n = int(input("Enter number:"))
while n >= 1:
    shesh = n % 10
    n = n // 10
    print(shesh, end="")