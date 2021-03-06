import pygame
import time
pygame.init()

clock = pygame.time.Clock()
fps_limit = 60.0

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption('Cul gras')

centre = (400,400)
posx = 400
posy = 400

#Vitesse linéare / vitesse diagonale
vit = 10
vitd = 5 


class Cercle:
    def __init__(self,color,radius,surface=screen,center=centre):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
    def dessin_cercle(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

running = True
while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    #circle = pygame.draw.circle(screen, (255,0,0), (posx, posy), 100)
    circle1 = dessin_cercle(screen, (255,0,0), centre, 75)
    
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