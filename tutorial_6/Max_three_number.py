a = int(input('Enter a number  '))
b = int(input('Enter a number : '))
c = int(input('Enter a number : '))
print('Max is = ', max(a, b, c))
if a >= b and a >= c:
    print(a, " is the maximum")
elif b >= a and b >= c:
    print(b, " is the maximum")
elif c >= a and c >= b:
    print(c, " is the maximum")
