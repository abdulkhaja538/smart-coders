hour = int(input())
minute = int(input())

hour = hour % 12

hour_angle = hour * 30 + minute * 0.5
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)

print("Angle:", angle)