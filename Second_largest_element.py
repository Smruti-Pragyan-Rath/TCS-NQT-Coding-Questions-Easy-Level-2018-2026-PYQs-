#Find the second largest element
n=int(input("Number of inputs"))
arr=[]
for i in range(0,n):
    a=int(input("Enter a number"))
    arr.append(a)
arr=set(arr)
arr=sorted(arr, reverse=True)
print(arr[1])
