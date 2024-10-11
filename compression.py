def compress (text):
    result = ""
    ctr = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            ctr = ctr + 1
        else:
            result += text[i-1]
            result += str(ctr)
            ctr = 1
    result += text[-1] + str(ctr)
    if len(result)>len(text):
        return text
    else:
        return result

text = input("Enter some text: ")
print(compress(text))