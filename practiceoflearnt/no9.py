# Is number is palindrome or not
def palind():
    print()
    typed_first = int(input("Type a number you want to check:"))
    mainnum = typed_first
    reversed_karela = 0
    while mainnum > 0:
        remain = mainnum % 10
        reversed_karela = (reversed_karela * 10) + remain
        mainnum = mainnum // 10

    if typed_first == reversed_karela:
        print("This number is palindrom number.")
    else:
        print("This number is not palindrom number.")


palind()





