import math

l = int(input('Enter the length '))
b = int(input('Enter a breadth '))
a = l * b
p = 2 * (l + b)
d = math.sqrt(l * l + b * b)
print('The area is = ', a)
print('The perimeter is = ', p)
print('The length of diagonal is = ', d)
