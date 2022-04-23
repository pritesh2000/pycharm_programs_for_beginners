def is_s1_in_s2(s1, s2):
    flag = True
    for i in s1:
        if i in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = is_s1_in_s2(s1, s2)

print(flag)
