str1 = "tPRadITEviSH"
lower = []
upper = []
for i in range(len(str1)):
    if str1[i].islower():
        lower.append(str1[i])
    else:
        upper.append(str1[i])
new_string = "".join(lower + upper)
print("Sorted string is:", new_string)
