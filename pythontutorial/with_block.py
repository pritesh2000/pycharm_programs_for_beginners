# f = open("pritesh2.txt")
# print(f.readlines())
# print(f.readline())
# f.close()

with open("pritesh2.txt") as f:
    a = f.readlines()
    print(a)

# f = open("pritesh4.txt", "a")
# print(f.readlines())
# f.close()