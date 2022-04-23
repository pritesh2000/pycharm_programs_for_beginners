N = int(input())
cmd = int(input('Which Comprehension You Wanna Make: \n'
                '1. List\n'
                '2. Dict\n'
                '3. Set\n'
                '-----> '))
if cmd == 1:
    a = [input(f'Enter Item {i + 1}: ') for i in range(N)]
    print(a)
elif cmd == 2:
    a = {i: f'{input(f"Enter Dictionary Value Here for Key {i + 1}: ")}' for i in range(N)}
    print(a)
elif cmd == 3:
    a = {input(f'Enter Item {i + 1}: ') for i in range(N)}
    print(a)
