a = "The name is Pritesh Tadvi"
b = 345
c = ["pritesh", "tadvi"]
d = {1: "manoj", 2: "raiga"}
e = (2, 4, 5, "dhak")

print(e, "\n")

c.reverse()                             # reverse function
print(c, "c\n")

reversed(d.items())                     # reversed function
for i in reversed(d.items()):
    print(i)


for i in range(5, 10, 2):               # range function   ( x, y , whichever gap you want within start and stop)
    print(i)

f = pow(3, 5, 33)                       # ( x to power y ) % z
print(f, "f\n")

g = round(23.34344434, 2)               # give number's nearest value (x, how many digit you want after number)
print(g, "\n")

x = globals()                           # globals give value of all the details
print(x["__file__"], "\n", x["__name__"], "\n", x["i"])

print("\n", len(a), "\n")               # length of string




