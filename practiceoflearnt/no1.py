# Calculation of number in sum and multiplication

def cal():
    if opr == 0:
        print("Multiplication is", n * m)
    elif opr == 1:
        print("Sum is", n + m)
    else:
        print("Enter proper input")


n = int(input("Enter first number:"))
m = int(input("Enter second number:"))
opr = int(input("Enter 0 for multiplication and 1 for sum:"))
cal()

