# Is first and last number is same in list
def first_last_same(lst):
    print("Given list is:", lst)
    first = lst[0]
    last = lst[-1]
    if first == last:
        return True
    else:
        return False


num = int(input("How long list you want, enter number:"))
lst = []
for i in range(0, num):
    lst.append(int(input(f"Enter number {i + 1}:")))
print("Result is", first_last_same(lst))
