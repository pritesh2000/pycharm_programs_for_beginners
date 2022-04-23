def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0


addition(10)
print(addition(10))

