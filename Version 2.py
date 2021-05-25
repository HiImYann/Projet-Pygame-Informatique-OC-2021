#VERSION 2 : Ajouts des commentaires et des images nécessaire au jeu

import pygame, random   #Importe les modules nécessaires

# -- Variables --

pygame.init()   #Initialise pygame et définit une horloge interne de 60 image par secondes
clock = pygame.time.Clock()
fps_limit = 60.0

#Valeur des dimensions de la fenêtre (dimensions de l'image de fond)
resx = 626
resy = 563
screen = pygame.display.set_mode([resx,resy]) #Définit la dimension de la fenêtre pour le programme

background_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\background_image_no_clouds.jpg') #Image de fond


# -- Classes --

#Image des 3 nuages différents
cloud_image_1 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud1.png') 
cloud_image_2 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud2.png')
cloud_image_3 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud3.png')

#Classes pour les 3 différents nuages
class Clouds1():
    def __init__(self): #Variables initiales
        self.position_x = 30
        self.position_y = 40

    def update(self): #L'affiche dans la boucle
        screen.blit(cloud_image_1,(self.position_x,self.position_y)) 


class Clouds2():
    def __init__(self):
        self.position_x = 210
        self.position_y = 50

    def update(self):
        screen.blit(cloud_image_2,(self.position_x,self.position_y))


class Clouds3():
    def __init__(self):
        self.position_x = 470
        self.position_y = 50

    def update(self):
        screen.blit(cloud_image_3,(self.position_x,self.position_y))
        

firecamp_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\firecamp.png') #Image de la bûche

class Firecamp(): #Classe du feu de camp
    def __init__(self):
        screen.blit(firecamp_image,(266,413)) #Affiche le feu de camp


# -- Objets --

Cloud1 = Clouds1()
Cloud2 = Clouds2()
Cloud3 = Clouds3()


# -- Listes --


# -- Game loop --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, [0, 0]) #Utilise l'image de fond choisie comme background


    #Affichage des nuages
    Cloud1.update()
    Cloud2.update()
    Cloud3.update()

    Firecamp() #Feu de camp

    pygame.display.set_caption("El Fuego    FPS : "+"{:.2f}".format(clock.get_fps())) #Affiche le nom de la fenêtre et les FPS
    pygame.display.flip()   
pygame.quit()