#find the prime numbers in a given range
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,Math.sqrt(n)+1):
        if n%i==0:
            return False
        else:
            return True
a=int(input("Enter the first number"))
b=in