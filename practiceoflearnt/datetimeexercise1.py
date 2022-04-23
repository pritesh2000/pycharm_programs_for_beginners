import datetime
# date and time
print(datetime.datetime.now())

# only time
print(datetime.datetime.now().time())

from time import gmtime, strftime

print(strftime("%Y-%m-%d %H:%M:%S ", gmtime()))
