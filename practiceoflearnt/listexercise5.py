list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

list3 = zip(list1, list2)
for i, j in list3:
    print(i, j)

for i, j in zip(list1, list2):
    print(i, j)
