lst1 = ["Alaska", "Alabama", "Arizone", "Arkansas", "Colorado", "Montana", "Nevada"]
lst2 = list(map(lambda x: x.count("a"), lst1))
print(lst2)
