count = 0
n = int(input("Enter number:"))
while n != 0:
    n = n // 10
    count += 1
print("Number of digit is:", count)
