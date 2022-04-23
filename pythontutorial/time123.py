import time

initial = time.time()
k = 0
print(initial)
while k < 4:
    print("I am pritesh tadvi and you know it")
    time.sleep(2)                       # pause program for given time
    k += 1
print("While loop ran in", time.time() - initial, "seconds\n")

initial2 = time.time()
for i in range(4):
    time.sleep(1)
    print("I am pritesh tadvi and you know it")
print("For loop ran in", time.time() - initial2, "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
