# This writes the stdin to the input file
import tempfile
import sys

_, filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
    f.write(sys.stdin.read())

# Write your code to read the file and print the result.
# use the variable filename for the name of the file.
with open(filename, 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())
st = [line.strip() for line in lines[1:]]
s1 = ''
k = 1
for s in st:
    for c in s:
        if c == '_':
            if k <= n:
                s1 += str(k)
                k += 1
            else:
                s1 += c
        else:
            s1 += c
    print(s1)