import pygame
import time
pygame.init()

clock = pygame.time.Clock()
fps_limit = 60.0

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption('Cul gras', clock)

posx = 400
posy = 400

#Vitesse linéare / vitesse diagonale
vit = 10 
vitd = 5 

color = (255,0,0)
radius = 10

'''
class Cercle:
    def __init__(self,color,radius):
        self.color = color
        self.radius = radius
    pygame.draw.circle(screen, color, (400,400), radius)'''

running = True
while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    circle = pygame.draw.circle(screen, (255,0,0), (posx, posy), 100)
    '''circle1 = Cercle((255,0,0),100)'''
    
    i = 0
    N = 0
    for i in range(10):
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(1+N, 1+N, 60, 60))
        i += 1
        N += 82


    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_LEFT]:
        posx -= vit

    if keys[pygame.K_RIGHT]:
        posx += vit

    if keys[pygame.K_DOWN]:
        posy += vit

    if keys[pygame.K_UP]:
        posy -= vit

    pygame.display.flip()
    
pygame.quit()