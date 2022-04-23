# f = open("pritesh2.txt", "w")  # w for replacement of written previous file and a for appending file content
# a = f.write("achcha hain hahaha\n")
# print(a)
# f.close()

# f = open("pritesh2.txt", "a")  # w for replacement of written previous file and a for appending file content
# a = f.write("achcha hain hahaha\n")
# print(a)
# f.close()

# Handle read and write both
f = open("pritesh2.txt", "r+")
print(f.read())
f.write("so jao bhai")
