#Perfect Number -> A number which is equal to the  sum of it's perfect divisors
def find_divisors(n):
    ans=[]
    for i in range(1,n):
        if(n%i==0):
            ans.append(i)
    return ans

n=int(input("Enter a number"))
div=find_divisors(n)
sum1=0
for i in div:
    sum1=sum1+i
if sum1==n:
    print("Perfect number")
else:
    print("Not a Perfect Number")