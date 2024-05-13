import math

n = int(input('Enter a number \n'))
sq = math.sqrt(n)
isq = int(sq)
if isq * isq == n:
    print('Perfect square')
else:
    print('Not a perfect sq')
