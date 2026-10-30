balance = float(input())
amount = float(input())

minimum_balance = 500

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < minimum_balance:
    print("Withdrawal rejected: minimum balance required")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)