keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = dict()

a = zip(keys, values)
print(a)
# If I put a's value in place of a then result will be as desired
for i, j in a:
    dic.update(a)

print(dic)

pynative_sol = dict(zip(keys, values))
print(pynative_sol)

seen_sol = dict()
for i in range(len(keys)):
    seen_sol.update({keys[i]: values[i]})

print(seen_sol)
