str1 = "P@yn2at&#i5ve"
char_count = 0
digit_count = 0
alphabet_count = 0
for char in str1:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        char_count += 1
print("Number of alphabet is:", alphabet_count)
print("Number of digit is:", digit_count)
print("Number of special character is:", char_count)

