import pygame, random   #Importe les modules nécessaires

# -- Variables --

pygame.init()   #Initialise pygame et définit une horloge interne de 60 image par secondes
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 626 #Valeur des dimensions de la fenêtre (dimensions de l'image de fond)
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

    def life(self): #Va être utile pour réduire la taille des particules graduellement
        self.radius -= 0.05


#Image des 3 nuages différents
cloud_image_1 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud1.png') 
cloud_image_2 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud2.png')
cloud_image_3 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud3.png')

#Classes pour les 3 différents nuages avec leur position
class Cloud1():
    def __init__(self,x,y):
        self.position_x = x
        self.position_y = y
        screen.blit(cloud_image_1,(x,y)) #Sert à afficher un objet qui contient une image

class Cloud2():
    def __init__(self,x,y):
        self.position_x = x
        self.position_y = y
        screen.blit(cloud_image_2,(x,y))

class Cloud3():
    def __init__(self,x,y):
        self.position_x = x
        self.position_y = y
        screen.blit(cloud_image_3,(x,y))


firecamp_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\firecamp.png') #Image de la bûche

class Firecamp():
    def __init__(self):
        screen.blit(firecamp_image,(250,413))



# -- Objets --

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
        next_particle_time = current_time + 5 

    Cloud1(30,40)
    Cloud2(220,50)
    Cloud3(470,50)

    Firecamp()

    for p in particles[:]:
        p.update()
        p.random_movement()
        p.life()
        if p.radius < 1:
            particles.remove(p)
    print(len(particles))

    pygame.display.set_caption("Le feuf    FPS : "+"{:.2f}".format(clock.get_fps())+"    n Particules : "+str(len(particles)))

    pygame.display.flip()   
pygame.quit()