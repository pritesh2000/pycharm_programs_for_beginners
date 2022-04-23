sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 11]
number_count = dict()
for i in sample_list:
    # print(number_count)
    # print(i)
    if i in number_count:
        number_count[i] = number_count[i] + 1
    else:
        number_count[i] = 1


print(number_count)
