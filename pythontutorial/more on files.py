f = open("pritesh2.txt")
# a = f.write("nacho\n")
# print(f.tell())
print(f.readline())
f.seek(98)
print(f.readline())
f.seek(0)
print(f.readline())

f.close()

