list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# list3 = list()
# for i, j in zip(list1, list2):
#     list3.append(i + j)

list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
