"""
Factorial
5!=1*2*3*4*5
6!=1*2*3*4*5*6

|  n  |
|     | =         n!
|  r  |        ---------
|     |        (n-r)!*r!
"""
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

if __name__=='__main__':
    n=int(input('Enter a number'))
    r=int(input('Enter a number'))
    print(factorial(n)/(factorial(n-r)*factorial(r)))
  