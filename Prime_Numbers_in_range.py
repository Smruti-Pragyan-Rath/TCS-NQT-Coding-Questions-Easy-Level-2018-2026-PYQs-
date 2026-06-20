#find the prime numbers in a given range
import math
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
a= int(input("Enter the first number"))
b= int(input("Enter the second number"))
ans=[]
for n in range(a,b+1):
    if(isPrime(n)):
        ans.append(n)
print(ans)


