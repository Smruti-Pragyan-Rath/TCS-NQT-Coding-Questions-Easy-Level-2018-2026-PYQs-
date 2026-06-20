#Find the repeated sum of digits until a single digit remains.

n=int(input("Enter the number"))
if n==0:
    ans=0
else:
    ans=1+(n-1)%9 #Quick Formula
print(ans) 