
def mod(x):
    if( x< 0):
        x = -x
        return 26 - x % 26
    
    else:
        return x % 26

def viginere(text, key, mode): #mode 1 for encrypt and -1 for decrypt
    cipher = ""
    for i in range(len(text)):
        x = ord(key[i % len(key)]) - 97 #normalizing to 0
        letter = ord(text[i]) - 97+ mode * x
        cipher += chr(mod(letter) + 97)
    
    print(cipher)

    
if __name__ == "__main__":

    text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    mode = int(input("Enter 1 for encrypt and -1 for decrypt: "))
    text.lower()
    text = text.replace(" ", "")
    viginere(text, key, mode)