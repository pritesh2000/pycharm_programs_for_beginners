# num = [12, 75, 150, 180, 145, 525, 50]
a = int(input("Enter number for length of matrix:"))
num = []
for i in range(a):
    l = int(input(f"Enter number {i + 1}:"))
    num.append(l)
for items in num:
    if items > 500:
        break
    elif items > 150:
        continue
    elif items % 5 == 0:
        print(items)

