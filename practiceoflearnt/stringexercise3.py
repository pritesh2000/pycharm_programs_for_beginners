s1 = "Proishe"
s2 = "rates"
# print(list(range(0, len(s1), 3)))
a = len(s1)
b = len(s2)
mid1 = int(a/2)
mid2 = int(b/2)
s3 = s1[0] + s2[0]
s3 += s1[mid1] + s2[mid2]
s3 += s1[int(a - 1)] + s2[int(b - 1)]
print(s3)
