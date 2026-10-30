def pattern(n, current=1):
    if current > n:
        return

    print(current, end=" ")
    pattern(n, current + 1)
    print(current, end=" ")


n = int(input())
pattern(n)