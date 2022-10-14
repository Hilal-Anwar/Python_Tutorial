s = ''
for i in range(0, 37):
    for j in range(0, 37):
        if (i % 4 == 0) or (j % 4 == 0):
            s = s + "██"
        else:
            s = s + "  "

    s = s + '\n'
print(s)
