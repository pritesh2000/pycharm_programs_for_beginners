# Number divisible by 5
lis = []
num = int(input("Enter number you desired for list:"))
for i in range(0, num):
    c = int(input(f"Enter number {i + 1}:"))
    lis.append(c)
print("Given list:", lis)

new_lis = []
for i in range(0, len(lis)):
    if lis[i] % 5 == 0:
        new_lis.append(lis[i])
print(new_lis)

for i in new_lis:
    print(i)
