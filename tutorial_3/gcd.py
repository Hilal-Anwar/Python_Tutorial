

a = int(input('Enter a number :'))
b = int(input('Enter a number :'))
mx = max(a, b)
mi = min(a, b)
while mx % mi != 0:
    tem=mi
    mi = mx % mi
    mx=tem

print(mi)
