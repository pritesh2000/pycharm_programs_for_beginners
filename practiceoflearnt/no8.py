# Forward triangle of number
n = int(input("Enter number you desired:"))
for i in range(n + 1):
    # print((i + 1)*(i + 1), str(i + 1))
    for j in range(i):
        print(i, end=" ")
    print()
