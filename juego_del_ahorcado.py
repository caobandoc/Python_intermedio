import os
from random import randint

TILDES = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),)

def normalize(word):
    for a, b in TILDES:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word.upper().strip('\n')


def returnWord():
    words = []
    with open("./archivos/data.txt","r",encoding="UTF-8") as f:
        for line in f:
            words.append(normalize(line))
    rnum = randint(0, len(words)-1)
    return words[rnum]
    
    
def adivinadas(word,wordA):
    lista = ""
    for x, y in word.items():
        try:
            if wordA.index(x) != -1:
                lista += y+" "
        except:
            lista += "_ "
    return lista


def encontro(word,letter,wordA):
    for x, y in word.items():
        if(y == letter):
            wordA.append(x)
    if len(word) == len(wordA):
        return False
    else:
        return True

    
def run():
    diviner = True
    word = dict(enumerate(returnWord()))
    wordA = []
    while(diviner):
        os.system("cls")
        print("¡Adivina la palabra!")
        print(word.values())
        print(adivinadas(word,wordA))
        letter = normalize(input("Ingresa una letra:"))
        diviner = encontro(word,letter,wordA)
    os.system("cls")
    print("Ganaste la palabra era " + "".join(word.values()))
    
    
if __name__ == '__main__':
    run()