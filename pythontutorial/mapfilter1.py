# --------------------map--------------------
# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num = [3, 5, 6, 7, 43, 4]
# square = list(map(sq, num))
# print(square)

# num = [3, 5, 6, 7, 43, 4]
# square = list(map(lambda x: x*x , num))
# print(square)

# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)

# -------------------------Filter-----------------------

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_greater_5(num):
#     return num>5
#
# greater_than_5 = list(filter(is_greater_5, list_1))
# print(greater_than_5)

# --------------------------Reduce-----------------------------
from functools import reduce

list1 = [1, 2, 3, 4, 8]

num = reduce(lambda x, y: x+y, list1)

# num = 0
# for i in list1:
#     num = num + i
print(num)

