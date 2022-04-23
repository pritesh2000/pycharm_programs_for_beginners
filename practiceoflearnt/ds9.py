speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# personal solution

# value = set()
# for i, j in speed.items():
#     print(j, end=" ")
#     value.add(j)
# print("\n", value)
# print(list(value))

# pynative solution

print("Dictionary value are:", speed.values())
speed_list = list()
for i in speed.values():
    if i not in speed_list:
        speed_list.append(i)

print("Unique list:", speed_list)