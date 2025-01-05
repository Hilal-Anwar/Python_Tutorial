# In this method digit is extracted from back
n = int(input("Enter a number :"))
rev = 0
tem = n
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

if rev == tem:
    print('Palendrome number')
else:
    print('not Palendrome number')
"""
   123/10
   
"""
