l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
odd = l1[1::2]
even = l2[0::2]
l3.extend(odd)
l3.extend(even)
print(l3)

# for i in l1:
#     if i % 2 == 1:
#         l3.append(i)
# for j in l2:
#     if j % 2 == 0:
#         l3.append(j)
# print(l3)
