#Largest Word in the sentence
sentence= "TCS NQT Coding Practice"
words=sentence.split()
length=[]
for i in words:
    length.append(len(i))
max_value=max(length)
index=length.index(max_value)
print(words[index])