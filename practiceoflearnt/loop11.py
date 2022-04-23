# Prime number from num 1 to num n 
start = int(input("Enter start number for prime number list:"))
end = int(input("Enter the number till you want prime number:"))
for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
