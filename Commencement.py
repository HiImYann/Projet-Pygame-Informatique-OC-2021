import pygame
import time
pygame.init()

clock = pygame.time.Clock()
fps_limit = 60.0

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption('Cul gras')

posx = 400
posy = 400
centre = (posx,posy)

#Vitesse
vit = 10

red = (255,0,0)

class Cercle:
    def __init__(self,color,radius,surface=screen,center=centre):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
    def dessin_cercle(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

cercle1 = Cercle(red,75,screen,(posx,posy))

running = True
while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    #circle = pygame.draw.circle(screen, (255,0,0), (posx, posy), 100)
    cercle1.dessin_cercle()
    
    i = 0
    N = 0
    for i in range(10):
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(1+N, 1+N, 60, 60))
        i += 1
        N += 82


    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_LEFT]:
        posx -= vit
        print("gauche")

    if keys[pygame.K_RIGHT]:
        posx += vit
        print("droite")

    if keys[pygame.K_DOWN]:
        posy += vit
        print("bas")

    if keys[pygame.K_UP]:
        posy -= vit
        print("haut")

    pygame.display.flip()
    
pygame.quit()