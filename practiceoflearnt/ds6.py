first_set = {23, 42, 65, 57, 78, 83, 29}
print("First set:", first_set)
second_set = {57, 83, 29, 67, 73, 43, 48}
print("Second set:", second_set)
section = set.intersection(first_set, second_set)
# section = first_set.intersection(second_set)
print("Intersection of first set and second set:", section)
# print(set.issubset(section, first_set))

for i in section:
    first_set.remove(i)

print("After removing above element from first set:", first_set)
