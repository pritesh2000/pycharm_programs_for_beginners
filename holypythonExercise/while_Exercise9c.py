lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]


def name_adder(lst):
    i = 0
    lst2 = []
    while i < len(lst):
        if lst[i] != "":
            lst2.append(lst[i])
        i += 1
    return lst2


print(name_adder(lst1))
