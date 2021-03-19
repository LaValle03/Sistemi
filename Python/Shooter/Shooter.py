import pygame
import random

# Random color script
a = random.randrange(1,255,1)
b = random.randrange(1,255,1)
c = random.randrange(1,255,1)
linecolor = a, b, c
#a bunch of variables
bgcolor = 0, 0, 0
x = y = 0
LEFT = 1
running = 1
s = 0
# b is number of shots fired
screen = pygame.display.set_mode((640, 400))
# defining image
image = pygame.image.load( "DK.bmp" )
imagePosition = image.get_rect()
imagePosition.bottom = 200
imagePosition.left = 300
screen.blit( image, imagePosition )
while running:
     event = pygame.event.poll()
     if event.type == pygame.QUIT:
         running = 0
     elif event.type == pygame.MOUSEMOTION:
         x, y = event.pos
     elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
         s = s + 1
        
         print ("\nYou fired shot number",s)
         print ("...at (%d,%d)!\n" % event.pos)
         
         pygame.mixer.init()
         shot = pygame.mixer.Sound("shot.wav")
         shot.play()

     pygame.display.set_caption("Shooter!")
     
     screen.fill(bgcolor)
     screen.blit( image, imagePosition )
     pygame.draw.line(screen, linecolor, (x, 0), (x, 399))
     pygame.draw.line(screen, linecolor, (0, y), (639, y))
     pygame.display.flip()
