import string
letterIndex = {}
pfmat = [ [0 for i in range(5) ] for j in range(5)]

def creatMat(key):
    i = 0
    letters = list(string.ascii_lowercase)
    letters.remove('j')
    
    for k in key:
        if(k == 'j'):
            k = 'i'
        pfmat[i // 5][ i % 5] = k
        letterIndex[k] = i
        i += 1
        if k in letters:
            letters.remove(k)

    for l in letters:
        if(i == 25):
            return
        pfmat[i // 5][ i % 5] = l
        letterIndex[l] = i
        i += 1
        

#mode 1 for encrypt -1 for decrypt
def mod(x, mode):
    x = x + mode
    if(x < 0):
        x = -(x)
        return 5 - x % 5
    else:
        return x % 5


def play(text, mode):
    #replace j with i
    text = text.replace('j', 'i')
    cipher = ""
    if(len(text) % 2 != 0):
        text += 'x'

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]
        row1 = letterIndex[a] //5
        row2 = letterIndex[b]//5
        col1 = letterIndex[a] % 5
        col2 = letterIndex[b] % 5

        if(letterIndex[a] % 5 == letterIndex[b] % 5): #same col
            cipher += pfmat[mod(row1, mode)][col1]
            cipher += pfmat[mod(row2, mode)][col2]
        elif(letterIndex[a] // 5 == letterIndex[b] // 5): #same row
            cipher += pfmat[row1][mod(col1, mode)]
            cipher += pfmat[row2][mod(col2, mode)]

        else: #diagonal
            cipher += pfmat[row1][col2]
            cipher += pfmat[row2][col1]

    return cipher


if __name__ == "__main__":
    text = input("Enter a text: ")
    key = input("Enter a key: ")
    mode = int(input("Enter 1 for encrypt and -1 for decrypt: "))
    text = text.replace(" ", "")

    creatMat(key.lower())
    print(f"cipher for {text} is {play(text.lower(), mode)}")
