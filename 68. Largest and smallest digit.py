n = abs(int(input()))

if n == 0:
    print("Largest:", 0)
    print("Smallest:", 0)
else:
    largest = 0
    smallest = 9

    while n:
        d = n % 10
        largest = max(largest, d)
        smallest = min(smallest, d)
        n //= 10

    print("Largest:", largest)
    print("Smallest:", smallest)