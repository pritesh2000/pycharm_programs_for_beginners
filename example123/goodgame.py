
# rahul singh
import random

print("This is a Snake water Gun game, hope you all know how to play")
lis = ["s", "w", "g"]
print("you have to enter one choice from three of them, s for snake, w for water and g for gun")


def game():

    userPoint = 0
    compPoint = 0
    chance = 5
    count = 1
    while (count <= chance):
        print("enter hare")
        user = input()
        computer = random.choice(lis)
        if (user == "s" or user == "w" or user == "g"):
            if (user == computer):
                print("tie")
            if (user == "s" and computer == "w"):
                userPoint += 1
                print(f"you won, point increased by 1, current {userPoint}")

            elif (user == "s" and computer == "g"):
                compPoint += 1
                print(f"computer won, current{compPoint} ")

            if (user == "w" and computer == "s"):
                compPoint += 1
                print(f"computer won, current {compPoint}")

            elif (user == "w" and computer == "g"):
                userPoint += 1
                print(f"you won, point increased by 1, current {userPoint}")

            if (user == "g" and computer == "s"):
                userPoint += 1
                print(f"you won, point increased by 1, current {userPoint}")

            elif (user == "g" and computer == "w"):
                compPoint += 1
                print(f"computer won, current {compPoint}")

            count = count + 1
        else:
            print("enter a valid character")
            break
    return (compPoint, userPoint)


while True:
    c, u = game()
    if (c < u):
        print(f"you won by {u} point")
    elif (c > u):
        print(f"you lose and computer won by {c} point")
    elif c == u:
        print("game tied")
    else:
        print("no result to show")
    print("game ended, if you want to play again then enter 1 else enter any key")
    take = input()
    if take == "1":
        continue
    else:
        break