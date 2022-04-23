# def func1():
#     print("I am back")
#
# func2 = func1
#
# del func1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
#
#
# a = funcret(1)
# print(a)


# def executer(func):
#     func("this")
#
#
# executer(print)


def dec1(func1):
    def now_exec():
        print("Executing now")
        func1()
        print("Executed")
    return now_exec


@dec1
def who_is_pritesh():
    print("I am Pritesh")       # this is decorator


# who_is_pritesh = dec1(who_is_pritesh)
who_is_pritesh()
