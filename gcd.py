def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a = [2,4,6]
result = a[0]
for i in a[1:]:
    result = gcd(result, i)

print(result)

