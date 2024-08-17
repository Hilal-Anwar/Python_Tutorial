n = int(input("Enter a number"))
t = n
while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10

if t == s:
    print("Palindrome number")
else:
    print("Not a palindrome number ")
