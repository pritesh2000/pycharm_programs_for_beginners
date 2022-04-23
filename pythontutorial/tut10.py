# dictionary is nothing but key value pairs
d1 = {}
word = [1, 2, 3]
print(type(d1))
d2 = {"pritesh": "bhajiya", "rohit": "vadapav", "ashish": "chips", "mukesh": {"a": "bidi", "b": "gutkha", "c": "cigaret"}}
print(d2["mukesh"]["b"])
print(d2)
d2["tu"] = (1, 3, 5)
d2[234] = "chuna"
del d2[234]
d2["ankit"] = "junk food"
print(d2)
d3 = d2.copy()
del d3["rohit"]
print(d3)
print(d2)
print(d2.get("pritesh"))
d2.update({"manan": "tablet"})
print(d2)
print(d2.keys())
print(d2.items())
