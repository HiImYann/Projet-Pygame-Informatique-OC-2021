import pygame, random

# -- Variables --

pygame.init()
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 1600 #Dimensions de la fenêtre, ici en 16/9
resy = 900
screen = pygame.display.set_mode([resx,resy]) #Définit la taille de la fenètre à 800 par 800 (pixels)

# -- Classes --

class Particule():
    def __init__ 


# -- Boucle du jeu --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.display.set_caption()

    pygame.display.flip()   
pygame.quit()