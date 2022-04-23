import time

print("Milliseconds of time:")
milliseconds = int(round(time.time() * 1000))
print(milliseconds)

# Just for fun
print("Without milliseconds:")
# without typecasting into integer
print(round(time.time()) * 1000)
print(int(round(time.time()) * 1000))
print(round(time.time()))

print(round(8, 12))
lit = round(8, 9)
print(lit)
print(milliseconds)
