import pygame
import sys

pavimento = [[0, 0, 0, -1, -1, 0, -1],
            [-1, 0, 0, 0, -1, -1, 0], 
            [0, 0, -1, -1, -1, 0, 0], 
            [-1, 0, 0, 0, -1, -1, 0], 
            [-1, 0, 0, 0, 0, -1, -1], 
            [-1, -1, -1, 0, 0, 0, -1]] 

dimensione = 100




#colori
NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)


def disegnaGriglia():
    for x in range(len(pavimento)):
        for y in range(len(pavimento[0])):
            rettangolo = pygame.Rect(x * dimensione, y * dimensione, dimensione, dimensione)

            if (pavimento[x][y] == 0):
               pygame.draw.rect(schermo, BIANCO, rettangolo, 1)
            elif (pavimento[x][y] == -1):
                pygame.draw.rect(schermo, ROSSO, rettangolo, 1)


def main():
    global schermo
    pygame.init()
    schermo = pygame.display.set_mode(len(pavimento[0] * dimensione), len(pavimento) * dimensione)
    schermo.fill(NERO)
    
    

    while True:
        disegnaGriglia()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
