lst1 = [1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]
lst2 = sorted(lst1, key=lambda x: x % 5, reverse=True)
print(lst2)
