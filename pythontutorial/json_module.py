import json
data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(parsed["var1"])
print(type(parsed))

# Task 1 - json.load ?

data2 = {
    "channel_name": "pritesh tadvi",
    "cars": ["bmw", "audi a8", "ferrari"],
    "fridge": ("rotii", 4, "bidi"),
    "isbad": False
}

jscomp = json.dumps(data2)      # now you can use it in javascript
print(jscomp)

# Task2 = what is sort keys parameter in dumps
