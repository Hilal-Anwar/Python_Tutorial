hours = int(input("Enter the number of hours"))
charge = 0
if hours <= 8:
    charge = 10
elif hours > 8 and hours <= 16:
    charge = 10 + (hours - 8) * 6
else:
    charge = 10 + 8 * 6 + (hours - 16) * 5

print("Amout to be paid is = ", charge)
