# Even index character appears
string = input("Enter text here:")
print("It will give even character of input")
word = list(string)
for i in word[0::2]:
    print(i)
