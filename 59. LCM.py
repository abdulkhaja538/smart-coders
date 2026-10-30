a = int(input())
b = int(input())

x, y = abs(a), abs(b)

while y:
    x, y = y, x % y

gcd = x

if gcd == 0:
    print(0)
else:
    print(abs(a * b) // gcd)