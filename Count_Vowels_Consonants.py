#Count the number of Vowels and Consonants
word=input("Enter the word")
word=word.upper()
Vowels=['A', 'E', 'I', 'O', 'U']
V=0
C=0
for i in word:
    if i in Vowels:
        V=V+1
C=len(word)-V
print("Vowels, consonants", V,C)