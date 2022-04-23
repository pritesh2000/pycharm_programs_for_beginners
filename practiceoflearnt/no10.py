# From two different list , add odd from list 1 and add even from list 2
# Then make new list by them
def fresh_list():
    new_list = []

    for k in range(len(list1)):
        if list1[k] % 2 == 1:
            new_list.append(list1[k])
    for j in range(len(list2)):
        if list2[j] % 2 == 0:
            new_list.append(list2[j])
    return new_list


n = int(input("Enter the length for first list you wanted:"))
list1 = []
for i in range(n):
    list1.append(int(input(f"Enter number {i + 1}:")))

m = int(input("Enter the length for second list you wanted:"))
list2 = []
for i in range(m):
    list2.append(int(input(f"Enter number {i + 1}:")))

print("First list:", list1)
print("Second list:", list2)

print("New list is:", fresh_list())
