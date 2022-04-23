list1 = [5, 20, 15, 20, 25, 50, 20]

# for i in list1:                   # Self
#     if i == 20:
#         list1.remove(i)
# print(list1)


# def remove_value(sample_list, value):       # Pynative1
#     return [i for i in list1 if i != value]
#
#
# print(remove_value(list1, 20))

while 20 in list1:                     # Pynative2
    list1.remove(20)

print(list1)
