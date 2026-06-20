#Decimal to binary
def decimal_to_binary(n):
    if n==0:
        return "0"
    binary=[]
    while n>0:
        rem=n%2
        binary.append(str(rem))
        n=n//2
    return "".join(binary[::-1])
b=decimal_to_binary(19)
print(b)


