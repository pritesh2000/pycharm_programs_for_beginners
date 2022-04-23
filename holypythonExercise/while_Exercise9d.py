lst1 = ["Sam", "", "Ben", "Olivia", "Alicia"]


def name_adder(lst):
    i = 0
    lst2 = []
    while i < len(lst):
        if lst[i] != "":
            lst2.append(lst[i])
        else:
            break
        i += 1
    return lst2


print(name_adder(lst1))
