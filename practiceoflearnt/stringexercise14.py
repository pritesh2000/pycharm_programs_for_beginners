str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# b = list(filter(None, str_list))
# print(b)

new_list = []
for i in str_list:
    if i:
        new_list.append(i)
print(new_list)
