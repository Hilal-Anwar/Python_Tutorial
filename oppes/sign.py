import math

a = int(input("Enter a number: "))
sq = a * a
r = math.sqrt(sq)
if r == a:
    print("positive")
else:
    print("negative")
