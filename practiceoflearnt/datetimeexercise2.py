from datetime import datetime
date_string = "Feb 25 2020 4:20PM"
dater = "Sep 30 2021 3:20AM"

datetime_object = datetime.strptime(dater, "%b %d %Y %I:%M%p")
datetime_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(datetime_object)
print(datetime_obj)
