#Count Even or Odd Digits
n=563248
m=list(str(n))
e=0
o=0
for i in m:
    if int(i)%2==0:
        e+=1
    else:
        o+=1
print(e,o)
