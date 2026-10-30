n = abs(int(input()))

if n == 0:
    print(1)
else:
    count = 0

    while n:
        count += 1
        n //= 10

    print(count)