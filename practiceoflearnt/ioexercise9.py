import os

space = os.stat("hello.txt").st_size
if space == 0:
    print("File is empty!!!")
