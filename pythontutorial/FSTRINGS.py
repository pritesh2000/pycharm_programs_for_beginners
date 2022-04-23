# F strings
me = "Pritesh"
a = "This is %s" % me
print(a)        # not a good practice

a1 = 3
a = "This is %s %s" %(me, a1)
print(a)        # neither it is

a = "This is {1} {0}"
b = a.format(me, a1)
print(b)

import math

a = f"This is {me} {a1} {math.cos(0)}"
print(a)