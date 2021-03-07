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

#Couleurs
red = (255,0,0)
orange = (255,150,0)
yellow = (255,255,0)
green = (0,255,0)
aqua = (0,255,200)
light_blue = (0,255,255)
blue = (0,0,255)
purple = (150,0,255)
pink = (255,0,255)



class Cercle():
    def __init__(self,couleur,rayon):
        pygame.sprite.Sprite.__init__(self)
        self.couleur = couleur
        self.rayon = rayon
        self.position_x = 400
        self.position_y = 400

    def update(self): #fonction executée à chaque frame pour afficher l'objet
        pygame.draw.circle(screen, self.couleur, (self.position_x,self.position_y), self.rayon)

    def mouvements(self,x,y):
        self.position_x += x
        self.position_y += y
        if self.position_x < 0 or self.position_x > 800 or self.position_y < 0 or self.position_y > 800:
            self.position_x = 400
            self.position_y = 400

cercle1 = Cercle(aqua,75)

running = True
while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    #circle = pygame.draw.circle(screen, (255,0,0), (posx, posy), 100)
    
    i = 0
    N = 0
    for i in range(10):
        pygame.draw.rect(screen, (pink), pygame.Rect(1+N, 1+N, 60, 60))
        i += 1
        N += 82

    if pygame.key.get_pressed()[pygame.K_UP] == True:
        cercle1.mouvements(0,-10)
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        cercle1.mouvements(10,0)
    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        cercle1.mouvements(0,10)
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        cercle1.mouvements(-10,0)

    cercle1.update()

    pygame.display.flip()
    
pygame.quit()