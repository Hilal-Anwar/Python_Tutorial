f = open('pattern.txt', 'w')
letters = 'abcdefghijklmnopqrstuvwxyz'
n = len(letters) // 2
for i in range(n):
    line = letters[i] + letters[-1 - i]
    if i != n - 1:
        line = line + '\n'
    f.write(line)
f.close()