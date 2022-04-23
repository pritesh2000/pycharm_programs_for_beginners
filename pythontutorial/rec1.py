# def factorial_iterative(k):
#     """
#     :param k : Integer
#     :return
#     """
#     fac = 1
#     for i in range(k):
#         fac = fac * (i + 1)
#     return fac
#
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# number = int(input("Enter the number"))
# print("Factorial in iterative method", factorial_iterative(number))
# print("Factorial in recursive method", factorial_recursive(number))

# quiz
def fibo1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    else:
        # for i in range(2, n):
        #     # a, b = b, a+b
        #     # i = fibo1(a) + fibo1(b)

        return fibo1(n-2) + fibo1(n-1)


num = int(input("Enter a number:"))
print("Fibonaci value is", fibo1(num))
