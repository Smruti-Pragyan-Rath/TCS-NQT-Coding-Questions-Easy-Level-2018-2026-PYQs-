#Print First N fibonacci numbers
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input("Enter N"))
for i in range(n):
    print(fib(i) , end=" ")