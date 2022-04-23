from datetime import datetime
given_date = datetime(2020, 7, 26)

print("Given day is:")
print(given_date.strftime("%A"))
print("Number of week is:")
print(given_date.today().weekday())
