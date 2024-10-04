def anagram(word1, word2):
    if(len(word1) != len(word2)):
        return False
    else:
        for i in range(len(word1)):
            if (word1.count(word1[i]) != word2.count(word1[i])):
                return False
        return True

print('Enter two words (separared by a space): ')
user = input()
words = user.split(' ')
if(len(words) != 2):
    print('invalid input!')
else: 
    print(f'anagram: {anagram(words[0], words[1])}')