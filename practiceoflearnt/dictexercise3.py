sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

for i in sampleDict.values():
    print(sampleDict)


print(sampleDict["class"]["student"]["marks"]["history"])

