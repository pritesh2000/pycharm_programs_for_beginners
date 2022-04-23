tuple1 = (45, 45, 45, 45)

# for i in tuple1:
#     if i == tuple1[0]:
#         print(True)


def same(k):
    return all(i == k[0] for i in k)


print(same(tuple1))
