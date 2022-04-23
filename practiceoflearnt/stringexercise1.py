str1 = "Pritesh"    # first, middle and last word
a = len(str1)
result = str1[0]
result += str1[int(a / 2)]
result += str1[int(a-1)]
print(result)

str2 = str1         # middle three word
mi = int(len(str2)/2)
# res = ""
# res += str2[int((a-2)/2)]
# res += str2[int(a/2)]
# res += str2[int((a+2)/2)]
res = str2[mi - 1: mi + 2]
print(res)
