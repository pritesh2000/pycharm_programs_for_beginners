def exp(base, power):
    result = 1
    num = power
    while num >= 1:
        result = result * base
        num -= 1
    print(f"{base} is base and {power} is power so result is:", result)
    return result


n = int(input("Enter base:"))
m = int(input("Enter power:"))

exp(n, m)
