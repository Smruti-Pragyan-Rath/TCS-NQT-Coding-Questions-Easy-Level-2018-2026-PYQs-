#Automorphic number -> A number whose square ends with the same number
n=int(input("Enter the number"))
num_digits=len(str(n))
square=n*n
x=square%(10 ** num_digits)
if x==n:
    print("Automorphic Number")
else:
    print("Not Automorphic")