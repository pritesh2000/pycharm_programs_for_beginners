def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec


@dec1
def who_is_pritesh():
    print("I am Pritesh")


# who_is_pritesh = dec1(who_is_pritesh)
who_is_pritesh()
