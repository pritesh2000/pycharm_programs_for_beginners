from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

given_date = datetime(2020, 2, 25)
print(given_date)

new_data = given_date + relativedelta(months=+ 4)
print(new_data)
