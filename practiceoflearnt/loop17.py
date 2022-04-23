sequence_sum = 0
n = 5
k = 2

for i in range(n):
    # for j in range(n):
    # sequence_sum = sequence_sum + (10 * i) + (k * i)
    print(k, end="+")
    sequence_sum += k
    k = k * 10 + 2

print(" : The answer is:", sequence_sum)
