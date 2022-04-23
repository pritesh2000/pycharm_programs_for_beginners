# Downward triangle pattern
n = int(input("Enter number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print(j + 1, end=" ")
    print()
