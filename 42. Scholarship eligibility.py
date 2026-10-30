marks = float(input())
attendance = float(input())
income = float(input())

if marks >= 80 and attendance >= 75 and income <= 300000:
    print("Eligible")
else:
    print("Not eligible")