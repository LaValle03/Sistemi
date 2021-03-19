import pygame
import sys

LANGHEZZA = 600
ALTEZZA = 800
SFONDO = (0,0,0)

schermo = pygame.display.set_mode((LANGHEZZA, ALTEZZA))
schermo.fill(SFONDO)

def main():
    global schermo
    pygame.init()


    while True:
        #codice



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()