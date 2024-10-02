#converts letters to lowercase and removes any non alphabetical characters
def cleaner(text):
    result = ""
    for i in range(0,len(text)):
        if (text[i].isalpha()):
            result += text[i].lower()
    return result

text = input("Enter a word: ")
cleaned = cleaner(text)
print(cleaned)