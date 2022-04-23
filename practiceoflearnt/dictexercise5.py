sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

new = dict()

# Keys to extract
keys = ["name", "salary"]

for i in keys:
    new.update({i: sample_dict[i]})

print(new)


new_dic = {i: sample_dict[i] for i in keys}     # Pynative solution
print(new_dic)
