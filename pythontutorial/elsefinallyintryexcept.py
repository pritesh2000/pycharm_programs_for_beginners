f1 = open("pritesh.txt")

try:
    f = open("does.txt")

except EOFError as e:
    print("EOError aa gaya hain", e)

except IOError as e:
    print("IOError aa gaya hain", e)

except Exception as e:
    print(e)

else:               # This will run if except is not running.
    print("This will run only if except is not running.")

finally:                # This will run anyway
    print("Rum this anyway...")
    f1.close()

print("Important stuff")
