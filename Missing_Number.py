#Missing Number in an Array
n=int(input("Enter N"))

expected_sum=(n*(n+1))//2
val=(list(map(int, input("Enter the number").split())))
ans=expected_sum-sum(val)
print(ans)