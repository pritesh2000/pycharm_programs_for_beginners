# Health management system

client_list = {1: "Pritesh", 2: "Mukesh", 3: "Mahesh"}
log_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print('Select Client Name:')
    for num, value in client_list.items():
        print("Press", num, "for", value, "\n", end="")
    client_name = int(input())
    """This is for only input of client"""

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())
    # This input is for in which you want to save your data

    if op == 1:
        for num, value in log_list.items():
            print(f"Press {num} for {value}")
        log_name = int(input())
        print("Selected Job:", log_list[log_name])
        with open(client_list[client_name]+"_"+log_list[log_name]+".txt", "a") as f:
            k = "y"
            while k != "n":
                print("Enter", log_list[log_name])
                textenter = input()
                f.write("["+str(getdate())+"]:" + textenter + "\n")
                k = input("Add more? y/n:")
                continue

    elif op == 2:
        for key, value in log_list.items():
            print(f"Press {key} to retrieve {value}")
        log_Name = int(input())
        print(client_list[client_name] + "\'s " + log_list[log_Name] + " Report")
        with open(client_list[client_name]+"_"+log_list[log_Name] + ".txt") as f:
            for line in f:
                print(line, end="")
    else:
        print("Invalid Input !!!")


except Exception as e:
    print("Wrong Input !!!")

