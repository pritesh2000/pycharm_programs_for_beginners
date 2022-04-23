# def calculation(num1, num2):
#     a = num1 + num2
#     b = num1 - num2
#     return a, b
#
#
# res = calculation(40, 10)
# print(res)
#

def calculation(a, b):
    return a + b, a - b


add, sub = calculation(40, 10)
print(add, sub)
print(calculation(40, 10))
