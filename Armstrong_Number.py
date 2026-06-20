#Armstrong number-> number whose sum of cube of each digits is equal to the number
n=input("Enter a number")
digits=[]
for i in n:
    digits.append(int(i))
sum1=0
for j in digits:
    sum1=sum1+(j**3)
if sum1==int(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")