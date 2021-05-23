import pygame, random   #Importe les modules nécessaires

# -- Variables --

pygame.init()   #Initialise pygame et définit une horloge interne de 60 image par secondes
clock = pygame.time.Clock()
fps_limit = 60.0

#Valeur des dimensions de la fenêtre (dimensions de l'image de fond)
resx = 626
resy = 563
screen = pygame.display.set_mode([resx,resy]) #Définit la dimension de la fenêtre pour le programme

next_particle_time = 0 #Crée une variable qui sera utilisée pour le créateur de particule

background_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\background_image_no_clouds.jpg') #Image de fond

# -- Classes --

class Particle():
    def __init__ (self,color,radius): 
        pygame.sprite.Sprite.__init__(self) #Nécessaire pour que python sache que c'est un sprite à afficher
        self.color = color
        self.radius = radius
        self.position_x = 313 
        self.position_y = 415

    def update(self): #Sert à mettre à jour/dessiner les particules
        pygame.draw.circle(screen, self.color, (self.position_x,self.position_y),self.radius)

    def random_movement(self): #Sert à donner un mouvement aléatoire aux particules
        self.position_x += random.randint(-2,2)
        self.position_y -= random.randint(0,1)

    def vent(self,x,y): #Donne un effet de vent aux particules quand on déplacera les nuages
        self.position_x += x
        self.position_y += y

    def life(self): #Va être utile pour réduire la taille des particules graduellement
        self.radius -= 0.05


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

    def mouvements(self,x,y): #Déplacements du nuage
        self.position_x += x
        self.position_y += y

    def bordure(self): #Si le nuage touche une des bordures, sa position est réinitialisée pour qu'ils ne disparaissent pas
        if self.position_x < 0:
            self.position_x = resx
        if self.position_x > resx:
            self.position_x = 0

class Clouds2():
    def __init__(self):
        self.position_x = 210
        self.position_y = 50

    def update(self):
        screen.blit(cloud_image_2,(self.position_x,self.position_y))

    def mouvements(self,x,y):
        self.position_x += x
        self.position_y += y

    def bordure(self):
        if self.position_x < 0:
            self.position_x = resx
        if self.position_x > resx:
            self.position_x = 0

class Clouds3():
    def __init__(self):
        self.position_x = 470
        self.position_y = 50

    def update(self):
        screen.blit(cloud_image_3,(self.position_x,self.position_y))

    def mouvements(self,x,y):
        self.position_x += x
        self.position_y += y

    def bordure(self):
        if self.position_x < 0:
            self.position_x = resx
        if self.position_x > resx:
            self.position_x = 0
        

firecamp_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\firecamp.png') #Image de la bûche

class Firecamp(): #Classe du feu de camp
    def __init__(self):
        screen.blit(firecamp_image,(266,413)) #Affiche le feu de camp


# -- Objets --

Cloud1 = Clouds1()
Cloud2 = Clouds2()
Cloud3 = Clouds3()

# -- Listes --

particles = [] #Crée une liste de particules pour le programme

# -- Game loop --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, [0, 0]) #Utilise l'image de fond choisie comme background
    random_color = (255,random.randint(0,180),0) #Couleurs aléatoire entre orange et rouge pour le feu

    current_time = pygame.time.get_ticks() #Donne le temps en millisecondes depuis que la loop a été commencée
    if current_time > next_particle_time: #Compare les deux temps pour ajouter une particule périodiquement
        particles.append(Particle(random_color,random.randint(0,10))) #Ajoute une particule à la liste avec les valeurs choisies
        next_particle_time = current_time + 15

    #Mouvement du vent pour les 3 nuages avec le clavier
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        Cloud1.mouvements(1,0)
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        Cloud1.mouvements(-1,0)
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        Cloud2.mouvements(1,0)
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        Cloud2.mouvements(-1,0)
    if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        Cloud3.mouvements(1,0)
    if pygame.key.get_pressed()[pygame.K_LEFT] == True:
        Cloud3.mouvements(-1,0)


    #Utilise update pour afficher les nuages et bordure pour la collision avec le bord de la fenêtre
    Cloud1.update()
    Cloud2.update()
    Cloud3.update()
    Cloud1.bordure()
    Cloud2.bordure()
    Cloud3.bordure()

    Firecamp() #Feu de camp

    for p in particles[:]: #Crée des particules en les ajoutant dans une liste
        p.update()
        p.random_movement() #Mouvement aléatoire des particules
        p.life() #Réduit la taille des particules
        if pygame.key.get_pressed()[pygame.K_LEFT] == True: #Déplace les particules vers la gauche (vent)
            p.vent(-0.6,0)
        if pygame.key.get_pressed()[pygame.K_RIGHT] == True: #Déplace les particules vers la droite (vent)
            p.vent(0.6,0)
        if p.radius < 1: #Supprime les particules qui sont plus petites que 1 pixel pour libérer la RAM
            particles.remove(p)

    pygame.display.set_caption("El Fuego    FPS : "+"{:.2f}".format(clock.get_fps())+"    n Particules : "+str(len(particles))) #Affiche le nom de la fenêtre, les FPS et le nombres de particules présentes 
    pygame.display.flip()   
pygame.quit()