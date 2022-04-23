from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given Data")
print(given_date)

sub_date = 7
sub = given_date - timedelta(sub_date)

# sub = given_date - timedelta(days=7)
print("New data")
print(sub)
