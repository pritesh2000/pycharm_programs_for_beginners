list1 = [["pritesh", 1], ["mitesh", 4], ["jignesh", 3], ["pratik", 2]]
dict1 = dict(list1)
# for yuo,numb in list1:
#   print(yuo,"find",numb)
print(dict1)
for item, chocolate in dict1.items():
    print(item, chocolate)
    print(item)

lung = [int, float, "scooter", "bike", "rickshaw", 2, 23, 46, 12, 234, 456]
for item in lung:
    if str(item).isnumeric() and item > 30:
        print(item)
