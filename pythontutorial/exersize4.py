
try:
    a = int(input("Enter a number:"))
    b = int(input("Enter either 0 or 1:"))
    i = 0
    c = "*"

    if b == 1:
        while i < a:
            i += 1
            print(c*i)
    elif b == 0:
        while i < a:
            print(c*a)
            a -= 1
    else:
        print("please enter 0/1 then run again.")


except Exception as e:
    print(e)
