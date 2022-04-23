from datetime import datetime, timedelta

print(datetime.now())

given_date = datetime(2020, 3, 22, 10, 0, 0)

print("Given Data")
print(given_date)
new_date = given_date + timedelta(days=7, hours=12)
print("Here 7 days and 12 hours added")
print(new_date)
