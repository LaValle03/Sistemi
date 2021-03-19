import pygame
import sys

#costanti colori e dimensioni della finestra pygame
NERO = (0,0,0)
BIANCO = (255,255,255)
LARGHEZZA = 250


#funzione che disegna su pygame il QR Code
def disegnaQR(codificatore, lista):
    for k in range(len(lista)):
        for j in range(5):
            rettangolo = pygame.Rect(j * 50, k * 50,50,50)
            if (lista[k][j] == 0):
                pygame.draw.rect(schermo, BIANCO, rettangolo)
            else:
                pygame.draw.rect(schermo, NERO, rettangolo)

#funzione che decodifica in binario una stringa seguendo il dizionario
def conversioneBinario(stringa, codificatore):
    lista = []
    for k in range (len(stringa)):
        lista.append(codificatore[stringa[k]])
    return lista

#funzione che legge il file e restituisce il contenuto sotto forma di stringa
def leggiFile(stringa):
    fileParola = open(stringa, "r")
    return fileParola.read()

#funzione che scrive su un file csv la liste di liste contenente la codifica in binario della stringa inserita precedentemente
def scriviListaFile(stringa, lista):
    file = open(stringa, "w")
    file.write(f"{lista}")
    file.close()


def main():
    scelta = input("0--> Tastiera\n1--> File\n")

    #scelgo se inserire la stringa da tastiera oppure da un file
    if int(scelta) == 0:
        stringa = input("Inserisci una stringa: ")

        #controllo se la stringa è troppo lunga
        while len(stringa) > 12:
            stringa = input("Inserisci una stringa: ")
    else:
        stringa = leggiFile("ciao.csv")

        #controllo se la stringa è troppo lunga
        if len(stringa) > 12:
            print("La stringa è troppo lunga")
            return
    
    #dizionario con chiave le lettere e i numeri. I valori sono liste in binario
    codificatore = {'a': [0,0,0,0,0], 'b': [0,0,0,0,1], 'c': [0,0,0,1,0], 'd': [0,0,0,1,1], 'e':[0,0,1,0,0], 'f':[0,0,1,0,1], 'g':[0,0,1,1,0], 'h':[0,0,1,1,1], 'i':[0,1,0,0,0], 'l':[0,1,0,1,0], 'm':[0,1,0,1,1], 'n':[0,1,1,0,0], 'o':[0,1,1,0,1], 'p':[0,1,1,1,0], 'q':[0,1,1,1,1], 'r':[1,0,0,0,0], 's':[1,0,0,0,1], 't':[1,0,0,1,0], 'u':[1,0,0,1,1], 'v':[1,0,1,0,0], 'z':[1,0,1,1,1], ' ':[1,1,0,0,0], '0':[1,1,0,0,1], '1':[1,1,0,1,0], '2':[1,1,0,1,1], '3':[1,1,1,0,0], '4':[1,1,1,0,1], '5':[1,1,1,1,0], '6':[1,1,1,1,1], '7':[1,0,1,1,0], '8':[1,0,1,0,1], '9':[0,1,0,0,1]}

    lista = conversioneBinario(stringa, codificatore)

    scriviListaFile("write.csv",lista)


    #pygame
    global schermo
    schermo = pygame.display.set_mode((LARGHEZZA, len(stringa) * 50))
    schermo.fill(NERO)
    pygame.init()


    while True:
        disegnaQR(codificatore, lista)

        #for che permette la chiusura della finestra pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()