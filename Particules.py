import pygame, random

# -- Variables --

pygame.init()
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 1600 #Dimensions de la fenêtre, ici en 16/9
resy = 900
screen = pygame.display.set_mode([resx,resy]) #Définit la taille de la fenètre à 800 par 800 (pixels)

# -- Objets --

# [location, velocity, timer]
particles = []


# -- Boucle du jeu --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    
    particles.append([[resx/2,resy/2],[random.randint(0,20) / 10 -1, -2], random.randint(4,6)])

    for particle in particles:
        particle[0] [0] += particle[1] [0]
        particle[0] [1] += particle[1] [1]
        particle[2] -= 0.1
        pygame.draw.circle(screen, (255,255,255), particle[0], particle[2])
        if particle[2] <= 0:
            particles.remove(particle)

    pygame.display.flip()   
pygame.quit()