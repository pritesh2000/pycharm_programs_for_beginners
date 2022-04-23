# This is Coroutines not function.
def searcher():
    import time
    # Some 4 seconds time-consuming task
    book = "This is a string of program in python in pycharm."
    time.sleep(4)

    while True:                 # From second time the function starts from here not from top.
        text = (yield)
        if text in book:
            print("Your text is in the book.")
        else:
            print("Your text is not in the book.")


search = searcher()         # Coroutines started
print("Search started.")
next(search)
print("Next method run")
search.send("program")
input("press any key...")
search.send("pycharm")
input("press any key...")
search.send("dance")
input("press any key...")
search.send("string")
input("press any key...")
search.send("news")

search.close()
