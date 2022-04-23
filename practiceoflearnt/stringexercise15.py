# Barabar khabar na padi
import string
import re
str1 = "/*Jon is @developer & musician"
new_str = str1.translate(str.maketrans('', '', string.punctuation))
print("Original string is:", str1)
print("Changed string is:", new_str)

str2 = "/*Jon is @developer & musician"
print("Original string is ", str2)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str2)
print("New string is ", res)



