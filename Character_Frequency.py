#Count frequency of each character
word=input("Enter string")
frequency={}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)
