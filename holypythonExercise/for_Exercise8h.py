dict1 = {"z1": 900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst = []
for i in dict1.values():
    if i > 1000:
        i -= 1000
        lst.append(i)
    else:
        lst.append(i)
print(lst)
