str1 = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


def count_a(a):
    c = 0
    for i in a.split():
        if i[0].lower() == 'a':

            c += 1
        else:
            pass
    return c


print(count_a(str1))
