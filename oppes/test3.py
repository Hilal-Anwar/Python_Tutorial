n = int(input('Enter the number of rows \n'))
s = ''
k = 2 * (n - 2) + 1
for i in range(n - 1):
    print(" " * i + "\\" + " " * k + "/")
    k -= 2
print(' ' * (n - 1) + 'v')

