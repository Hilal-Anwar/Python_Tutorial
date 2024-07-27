import math

a = int(input("Enter a number "))
sqt = int(math.sqrt(a))
if sqt * sqt == a:
    print("Perfect square")
else:
    print("Not a perfect square")
