str1 = "Emma25 is Data scientist50 and AI Expert"
temp = str1.split()
res = []
for item in temp:
    if any(j.isalpha() for j in item) and any(j.isdigit() for j in item):
        res.append(item)

print("Display words with alphabet and digit:")

for i in res:
    print(i)
