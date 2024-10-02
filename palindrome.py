def palindrome(text):
    is_palindrome = True
    j = len(text)-1
    for i in range(0,len(text)):
        if(text[i].lower() != text[j].lower()):
            is_palindrome = False
        j = j-1
    return is_palindrome 

print("Enter a word")
word = input()
if (palindrome(word)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")