#Harshad Number-> A number is harshad if it is divisible by the sum of its digits 
#2018
n=int(input("Enter the number"))
p=n
sum_n=0
while n>0:
    rem=n%10
    sum_n=sum_n+rem
    n=n//10
if p%sum_n==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
