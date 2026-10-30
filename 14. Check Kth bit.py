n = int(input())
k = int(input())

if n & (1 << k):
    print("Set")
else:
    print("Not set")