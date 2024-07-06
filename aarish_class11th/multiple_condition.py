n = int(input("Enter a number"))
if n % 2 == 0 and n >= 20:
    print("Even and greater than 20")
else:
    if n % 2 == 0:
        print("Number is even but less than 20")
    else:
        print("Number is odd and less than 20")
