def share(word1, word2):
    common = []
    for i in range (len(word1)):
        if (word2.count(word1[i]) > 0):
            common.append(word1[i])
    commons = set(common)
    return commons

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')
print(share(word1, word2))