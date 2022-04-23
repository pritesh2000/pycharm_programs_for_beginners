# Guess the number

number_of_guess = 0
print("You can guess number only 9 times:\n")
while number_of_guess < 9:
    n = int(input("Enter guessed number:"))
    if n > 18:
        print("Number is greater than actual number")
    elif n < 18:
        print("Number is less than actual number")

    else:
        print("You won")
        print(number_of_guess + 1, "Number of guess he took to finish")
        break
    number_of_guess = number_of_guess + 1
    print(9 - number_of_guess, "no. of time you can try")
    print(number_of_guess, "no. of try you have done\n")

if number_of_guess >= 9:
    print("Game over")
