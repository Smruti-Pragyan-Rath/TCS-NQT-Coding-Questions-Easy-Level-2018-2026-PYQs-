#Strong Numbers-A number is strong number if sum of factorials of digits is same as number
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

n=input("Enter the number")
p=int(n)
digits=[]
for i in n:
    digits.append(int(i))
sum1=0
for j in digits:
    sum1+=factorial(j)
if sum1==p:
    print("Strong Number")
else:
    print("Not a strong Number")

