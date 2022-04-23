l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = int(len(l1)/3)
start = 0
end = chunk_size
print("Original list is:", l1)
for i in range(3):
    indexes = slice(start, end)
    # print(indexes)
    a = l1[indexes]
    print("Chunk", i + 1, "is", a)
    a.reverse()
    print("After reversing chunk", i + 1, "is", a)
    start = end
    end = end + chunk_size
