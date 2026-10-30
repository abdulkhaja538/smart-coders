def digit_square_sum(n):
    total = 0

    while n:
        d = n % 10
        total += d * d
        n //= 10

    return total


n = int(input())
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    n = digit_square_sum(n)

if n == 1:
    print("Happy number")
else:
    print("Not a happy number")