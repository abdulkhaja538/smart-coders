n = int(input())

original = n
digits = len(str(abs(n)))

total = 0
temp = abs(n)

while temp:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == abs(original):
    print("Armstrong")
else:
    print("Not Armstrong")