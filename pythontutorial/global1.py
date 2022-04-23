"""
l = 10 # Global

def func1(n):
    # l = 5  # local
    m = 9  # local
    global l
    l = l + 34
    print(l, m)
    print(n, "This is local")
func1("This is me")
print(l)
"""

def harry():
    x = 20
    def rohan():
        global x    # global key word will get function from here so print (just making x global)
        x = 88
    print("Before calling rohan()", x) #
    rohan()         
    print("After calling rohan()", x)
harry()
print(x)











