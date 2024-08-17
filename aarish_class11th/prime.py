n = int(input("Enter a number"))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c = c + 1

    if c == 2:
        print("Prime number")
    else:
        print("Not a prime number")
