lst1 = [100, 200, 300, 400, 500]
lst2 = [1, 10, 100, 1000, 10000]

lst3 = list(map(lambda x, y: x + y, lst2, lst1))
print(lst3)
