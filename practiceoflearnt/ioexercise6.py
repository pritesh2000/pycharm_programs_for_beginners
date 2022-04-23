with open("file.txt", "r") as f:
    line = f.readlines()

with open("new_file.txt", "w") as f:
    count = 0
    for l in line:
        if count == 4:
            count += 1
            continue
        else:
            f.write(l)

        count += 1
