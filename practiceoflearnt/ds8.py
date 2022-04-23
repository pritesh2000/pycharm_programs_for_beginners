roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
rol_number = []
# for key, value in sample_dict.items():    # just experiment
#     if True:
#         print(value)
#         roll_number.remove(value)

for i in roll_number:                       # 1
    if i in sample_dict.values():
        # print(sample_dict.values)
        rol_number.append(i)

# roll_number[:] = [item for item in roll_number if item in sample_dict.values()]     # 2
print("Original list:", roll_number)
print("After removing unwanted element from list:", rol_number)
