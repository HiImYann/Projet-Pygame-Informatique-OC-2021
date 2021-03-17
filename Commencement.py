import pygame, time, random

# -- Variables --

pygame.init()
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 1600 #Dimensions de la fenêtre, ici en 16/9
resy = 900
screen = pygame.display.set_mode([resx,resy]) #Définit la taille de la fenètre à 800 par 800 (pixels)

posx = 0 #Variable position pour permettre aux objets de bouger
posy = 0
centre = (resx/2,resy/2)

vit = 10 #Vitesse

#Couleurs
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,150,0)
yellow = (255,255,0)
green = (0,255,0)
aqua = (0,255,200)
light_blue = (0,255,255)
blue = (0,0,255)
purple = (150,0,255)
pink = (255,0,255)


# -- Classes --

class Cercle():
    def __init__(self,couleur,rayon):
        pygame.sprite.Sprite.__init__(self)
        self.couleur = couleur
        self.rayon = rayon
        self.position_x = resx/2
        self.position_y = resy/2

    def update(self): #fonction executée à chaque frame pour afficher l'objet
        pygame.draw.circle(screen, self.couleur, (self.position_x,self.position_y), self.rayon)

    def mouvements(self,x,y):
        self.position_x += x
        self.position_y += y
        '''if self.position_x < 0 or self.position_x > 800 or self.position_y < 0 or self.position_y > 800:
            self.position_x = 1600
            self.position_y = 900'''


# -- Objets --

cercle1 = Cercle(aqua,75)

timedepart = 0

# -- Boucle du jeu --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    #circle = pygame.draw.circle(screen, (255,0,0), (posx, posy), 100)
    
    
    time = float(pygame.time.get_ticks())
    
    if time - timedepart > 1000:
        pygame.draw.rect(screen, (pink), (random.randint(0,1600),random.randint(0,900),60,60))

        
        

    if pygame.key.get_pressed()[pygame.K_UP] == True:
        cercle1.mouvements(0,-10)
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        cercle1.mouvements(10,0)
    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        cercle1.mouvements(0,10)
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        cercle1.mouvements(-10,0)

    cercle1.update()

    print(pygame.time.get_ticks())
    

    pygame.display.flip()
    
pygame.quit()