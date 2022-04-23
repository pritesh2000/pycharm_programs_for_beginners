# Tax calculation
salary = int(input("Enter your salary:"))
if salary <= 10000:
    tax = 0
elif salary <= 20000:
    tax = (salary - 10000) * 10 / 100
else:
    tax = 0 + 10000 * 10 / 100 + (salary - 20000) * 20 / 100

print("Your payable tax is:", tax)

