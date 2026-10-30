choice = input("Enter C for Celsius or F for Fahrenheit: ").upper()
temp = float(input("Temperature: "))

if choice == "C":
    print("Fahrenheit:", (temp * 9 / 5) + 32)
elif choice == "F":
    print("Celsius:", (temp - 32) * 5 / 9)
else:
    print("Invalid choice")