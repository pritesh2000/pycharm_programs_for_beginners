# Remove fix character from entered word
def removechar():
    enter = input("Enter word here:")
    # enter = "readitagain"
    # Enter = list(enter)
    ranje = int(input("Enter the number till you want to remove from text you entered:"))
    if ranje <= len(enter):
        print(enter[ranje:])
    else:
        print("This is not suitable number you entered for, so try again")


removechar()
