n = int(input())

for i in range(1, n + 1):
    for j in range(1, 2 * n):
        distance = abs(n - j)

        if distance <= i - 1:
            if distance == i - 1 or i == n:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")

    print()