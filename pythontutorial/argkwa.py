def funargs(noemal, *args, **kwargs):     # this sequence should be maintained
    print(noemal)
    print(args[0])
    print(type(args))
    print(type(kwargs))
    for i in args:
        print(i)
    print("\nNow I would like to introduce some of our heroes")
    for ket, value in kwargs.items():
        print(f"{ket} is {value}")


hat = ["Pritesh", "Rohan", "Skillsh", "Hammad", "Shivam"]
noemal = "I am a normal argument and this are the students:"
kw = {"Rohan": "Monitor", "Shivam": "Coordinator", "Pritesh": "Boss"}

funargs(noemal, *hat, **kw)
