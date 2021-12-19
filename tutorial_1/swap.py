a = [3, 21, 5, 6, 14, 8, 14, 3]
temp = 0
i = 0
while i < len(a) - 1:
    if a[i] % 7 == 0:
        temp = a[i + 1]
        a[i + 1] = a[i]
        a[i] = temp
        i = i + 2
    else:
        i = i + 1
print(a)
