set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

a = set1.intersection(set2)
print(a)

if set1.isdisjoint(set2):
    print("Two sets have no common values.")
else:
    print("Common values are:", set1.intersection(set2))
    