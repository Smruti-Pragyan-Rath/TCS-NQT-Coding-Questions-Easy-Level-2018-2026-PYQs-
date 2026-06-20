#check whether the number is pallindrome
n=input("Enter number")
rev_n=n[::-1]
if int(n)==int(rev_n):
    print("True")
else:
    print("False")