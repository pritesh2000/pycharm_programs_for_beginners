# Reverse number with space
n = int(input("Enter your desired number:"))
while n > 0:
    digit = n % 10
    n = n // 10
    print(digit, end=" ")