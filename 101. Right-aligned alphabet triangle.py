n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i):
        print(chr(ord('A') + j), end=" ")

    print()