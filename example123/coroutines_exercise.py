def read_letters():
    import time
    f = open("pynative.txt")
    time.sleep(3)
    content = f.read()
    while True:
        name = (yield)
        if name in content:
            print("Your name has been found.")
        else:
            print("Your name has not been found.")


try:
    search = read_letters()
    print("Reading Started...")
    next(search)
    print("Next method run...")
    m = 0
    while m == 0:
        print("Give input name that you wanted to search:")
        identity = str(input())

        search.send(identity)
        print("Do you want to search again???"
              "\nType 0 for no and 1 for yes.")
        s = 0
        while s == 0:
            n = int(input())
            if n == 1:
                s += 1
            elif n == 0:
                m += 1
                s += 1
            else:
                print("Please choose either 0 or 1:")
                continue
except Exception as e:
    print(e)
