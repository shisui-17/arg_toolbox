def Caesar_Encrypt(key, text):
    result = ""
    for i in text:
        if i.isupper(): result += chr((ord(i)+key-65) % 26 + 65)
        elif i.islower(): result += chr((ord(i)+key-97) % 26 + 97)
        else: result += i
    return result

def Caesar_Decrypt(key, text):
    result = ""
    for i in text:
        if i.isupper(): result += chr((ord(i) - key - 65) % 26 + 65)
        elif i.islower(): result += chr((ord(i) - key - 97) % 26 + 97)
        else: result += i
    return result

def Vigenere_Encrypt():
