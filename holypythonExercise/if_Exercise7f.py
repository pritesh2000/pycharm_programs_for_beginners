str1 = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


def count_l(a):
    c = 0
    for i in a.split():
        if "l" in i:
            c += 1
        else:
            pass
    return c


print(count_l(str1))

