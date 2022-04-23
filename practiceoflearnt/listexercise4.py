list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# list3 = list()
# for i in list1:
#     for j in list2:
#         list3.append(i + j)

list3 = [i + j for i in list1 for j in list2]
print(list3)
