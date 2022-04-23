from datetime import datetime
given_date = datetime(2020, 2, 25)

print(str(given_date))

string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)
