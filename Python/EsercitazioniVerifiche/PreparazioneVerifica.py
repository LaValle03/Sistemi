import pygame
import random
import sys

NERO = (0,0,0)
BIANCO = (255,255,255)
VERDE = (0,255,0)
ROSSO = (255,0,0)

dimensioni = (600,600)
schermo = pygame.display.set_mode(dimensioni)
schermo.fill(NERO)

def disegnaGriglia():
    for x in range(60):
        for y in range(60):
            rettangolo = pygame.Rect(x * 10, y * 10, 10, 10)

            pygame.draw.rect(schermo, BIANCO, rettangolo, 1)


def disegnaPercorso(dizionario):
    for k in range(60):
        bob = pygame.Rect(dizionario[k][0] + 300,dizionario[k][1] + 300,10,10)
        pygame.draw.rect(schermo, VERDE, bob)
    
    bob = pygame.Rect(300,300,10,10)
    pygame.draw.rect(schermo, ROSSO, bob)

def salvaFile(dizionario):
    file = open("percorso.csv", "w")

    for k in range (60):
        file.write(f"{k + 1} : {dizionario[k][0]},{dizionario[k][1]} \n")
    



def main():
    dizionario = {}
    x = 0
    y = 0

    for k in range (60) :
        rand = random.randint(0,3)

        dizionario[k] = [x, y]

        if rand == 0 :
            x = x - 10
        elif rand == 1 :
            x = x + 10
        elif rand == 2 :
            y = y - 10
        elif rand == 3 :
            y = y + 10

    salvaFile(dizionario)

    print(dizionario)
    #pygame

    global schermo
    pygame.init()
    
    

    while True:
        disegnaGriglia()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        disegnaPercorso(dizionario)

    


main()