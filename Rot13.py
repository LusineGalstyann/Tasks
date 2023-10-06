def rot13(text):
    new_text=''
    for i in text:
        if i.isupper():
            new_text += chr((ord(i) - 65 + 13) % 26 + 65)
        elif i.islower():
            new_text += chr((ord(i) - 97 + 13) % 26 + 97)
        else:
            new_text+=i
    return (new_text)