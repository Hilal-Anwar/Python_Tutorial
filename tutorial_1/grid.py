s = ''
for i in range(0, 76):
    for j in range(0, 76):

        if (i % 5 == 0) or (j % 5 == 0):
            s = s + '██'

        else:
            s = s + '  '

    s = s + '\n'
print(s)
