n = int(input())

original = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")