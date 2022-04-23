def thedecimal(i):
    if i - int(i) != 0:
        return i - int(i)
    else:
        return "INTEGER"


print(thedecimal(9.0))
print(9.9)

m = 9.9
print(m - int(m))
