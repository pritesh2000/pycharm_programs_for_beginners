sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_new = list()
for i in sample_list:             # personal logic
    if i not in sample_new:
        sample_new.append(i)

# sample_new = list(set(sample_list))       # not very good though pynative logic

print(sample_new)
print(tuple(sample_new))
m = tuple(sample_new)
print("Minimum number is:", min(m))
print("Maximum number is:", max(m))
# print("Maximum number is:", max(sample_list))

