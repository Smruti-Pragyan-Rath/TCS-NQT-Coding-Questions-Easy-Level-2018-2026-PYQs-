#Find GCD and LCM
import math
def gcd_manually(m,n):
    while n!=0:
        m,n=n,m%n 
    return m
def lcm_manually(m,n):
    return (m*n)//gcd_manually(m,n)
m=int(input("Enter 1st number"))
n=int(input("Enter 2nd number"))
print(math.gcd(m,n))
print(math.lcm(m,n))
print(gcd_manually(m,n))
print(lcm_manually(m,n))
