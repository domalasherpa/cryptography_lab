
def mod(x):
    if( x< 0):
        x = -x
        return 26 - x % 26
    
    else:
        return x % 26

def ceaser(text, key, mode):

    cipher = ""
    for t in text:
        letter = ord(t) - 97 + mode * key
        cipher += chr(mod(letter) + 97)
    
    print(cipher)

if __name__ == "__main__":
    text = input("Enter the plain text: ")
    key = int(input("Enter the key: "))
    mode = int(input("Enter 1 for encrypt and -1 for decrypt: "))
    text.lower()
    text = text.replace(" ", "")
    ceaser(text, key, mode)
