hours = float(input())
rate = float(input())

if hours <= 40:
    salary = hours * rate
else:
    normal = 40 * rate
    overtime = (hours - 40) * rate * 1.5
    salary = normal + overtime

print("Salary:", salary)