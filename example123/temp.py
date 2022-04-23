import pandas as pd
data = {"heppy": {1: "lol", 2: "dice"}, "fine": [1, 3, 5]}
a = data.keys()
print(a)
for v in data.values():
    print(type(v))
pd.DataFrame.from_dict(data["heppy"])
