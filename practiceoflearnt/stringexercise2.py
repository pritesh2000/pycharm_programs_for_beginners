s1 = "prsh"
s2 = "ite"
print("Before appending name are", "\"", s1, "\"", "and", "\"", s2, "\"")
a = len(s1)
b = int(a / 2)
s3 = s1[:b]
s3 += s2
s3 += s1[b:]
print("After appending name is:", s3)
