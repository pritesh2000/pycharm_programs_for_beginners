lst = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

# lst.sort(key=lambda x: x[2])
lst = sorted(lst, key=lambda x: x[1])
print(lst)
