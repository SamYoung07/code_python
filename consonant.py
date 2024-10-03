word = input("Enter a word: ")
vowels = 0
letters = 0
vowels += word.count('a')
vowels += word.count('e')
vowels += word.count('i')
vowels += word.count('o')
vowels += word.count('u')
print(vowels)
for i in range (len(word)):
    if (word[i].isalpha()):
        letters = letters + 1
print (f"Consonants: {letters-vowels}")