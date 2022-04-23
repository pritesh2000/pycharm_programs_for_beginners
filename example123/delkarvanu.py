list1 = []
print("How many Elements you want in the List")
n = int(input())
print("Enter the Elements")
for i in range(n):
    list1.append(input())
print("""Select through which comprihension you want to print
1. List comprehesion
2. Dictinary comprehension
3. Set comprehension
4. Generator comprehension""")
selected = int(input())

if(selected == 1):
    com = [i for i in list1]
    print(com)
    print(type(com))
elif(selected == 2):
    com = {i:f"Item {i}" for i in list1}
    print(com)
    print(type(com))
elif(selected == 3):
    com = {i for i in list1}
    print(com)
    print(type(com))
elif(selected == 4):
    com = (i for i in list1)
    for item in com:
        print(item)
    print(type(com))
