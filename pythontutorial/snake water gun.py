import random

d = ["s", "w", "g"]
turn = 10
no_of_turn = 0
computer_point = 0
user_point = 0

print("\t\t\tSnake-Water-Gun game\n")
print("s for Snake\nw for Water\ng for Gun\n")


while no_of_turn < turn:

    a = input("Snake,Water,Gun:")
    choice = a.lower()
    rand = random.choice(d)

    if rand == choice:
        print("Game tie.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    elif choice == "s" and rand == "g":
        computer_point += 1
        print(f"Your move is {choice} and computer's move is {rand}.")
        print("Thus computer wins 1 point.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    elif choice == "s" and rand == "w":
        user_point += 1
        print(f"Your move is {choice} and computer's move is {rand}.")
        print("So you win here 1 point.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    elif choice == "w" and rand == "s":
        computer_point += 1
        print(f"Your move is {choice} and computer's move is {rand}.")
        print("Thus computer wins 1 point.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    elif choice == "w" and rand == "g":
        user_point += 1
        print(f"Your move is {choice} and computer's move is {rand}.")
        print("So you win here 1 point.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    elif choice == "g" and rand == "w":
        computer_point += 1
        print(f"Your move is {choice} and computer's move is {rand}.")
        print("Thus computer wins 1 point.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    elif choice == "g" and rand == "s":
        user_point += 1
        print(f"Your move is {choice} and computer's move is {rand}.")
        print("So you win here 1 point.")
        print(f"Your point is {user_point} and computer point is {computer_point}.\n")

    else:
        print("You entered wrong input\n")
        continue

    no_of_turn += 1
    print(f"You have {turn - no_of_turn} chance left out of {turn}.")

print("\nGame over!!!")

if user_point == computer_point:
    print("\nGame is tie.")

elif user_point > computer_point:
    print("\nYou won the game.")

else:
    print("\nComputer won the game.")

