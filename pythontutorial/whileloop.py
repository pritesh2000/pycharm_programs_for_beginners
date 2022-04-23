# while loop
i = 0  # can't understand code right now while executing both while loop
while i < 45:
    print(i, end="  ")
    i = i + 1

# break and continue

while True:  # here i understand the code
    if i <= 55:
        i = i + 1
        continue

    print(i + 1, end="  ")
    if i == 66:
        break  # stop the loop
    i = i + 1
