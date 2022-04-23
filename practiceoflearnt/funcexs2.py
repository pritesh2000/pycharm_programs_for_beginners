def func1(*args):
    for i in args:
        print(i)
    print(type(args))
    print(har)


har = ["Pritesh", "is", "me"]
func1(20, 30, 40)
func1(80, 499, *har)
