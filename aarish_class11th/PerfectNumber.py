"""
sum of the factors of number=number 
perfect number
1+2+3+4+5+6
"""
num=int(input('Enter a number'))
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
    
if s==num:
    print('Perfect number')
else:
    print('Not a perfect number')