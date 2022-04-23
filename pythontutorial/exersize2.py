# faulty_calculater

x = int(input("Enter first number:"))
opr = input("Enter an operator :")
y = int(input("Enter second number:"))
# x, opr, y = (int(input("first")), input("operator"), int(input("second")))

if opr == '+':
    if x == 56 and y == 9:
        print(77)
    else:
        print("addition is", x + y)

elif opr == "-":
    print("subtraction is", x - y)

elif opr == "*":
    if x == 45 and y == 3:
        print(555)
    else:
        print("multiplication is", x * y)

elif opr == "/" and y != 0:
    if x == 56 and y == 6:
        print(4)
    else:
        print("division is", x / y)
else:
    print("give proper value")


