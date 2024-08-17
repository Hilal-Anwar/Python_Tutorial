a = int(input("Enter a number"))
b = int(input("Enter a number"))
if a % 2 == 0 or b % 2 == 0:
    if a % 2 == 0:
        print(a, "is a even number")
    if b % 2 == 0:
        print(b, "is a even number")
else:
    print("Both numbers are odd")