first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
a = first_set.issubset(second_set)
b = first_set.issuperset(second_set)
c = second_set.issubset(first_set)
d = second_set.issuperset(first_set)
print("First set is subset of second set:", a)
print("First set is superset of second set:", b)
print("Second set is subset of first set:", c)
print("Second set is superset of first set:", d)
if a is True:
    first_set.clear()
if c is True:
    second_set.clear()

print("First set:", first_set)
print("Second set:", second_set)
