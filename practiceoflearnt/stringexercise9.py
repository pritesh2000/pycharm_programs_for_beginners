str1 = "PYnative29@#8496"
addition = 0
count_num = 0
for i in str1:
    if i.isdigit():
        a = int(i)
        count_num += 1
        addition += a
print("Sum is:", addition)
print("Average is:", addition / count_num)
