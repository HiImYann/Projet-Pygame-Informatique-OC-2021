import pygame, random

pygame.init()   #Initialise pygame et définit une horloge interne de 60 image par secondes
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 600
resy = 600
screen = pygame.display.set_mode([resx,resy])

next_particle_time = 0

class Pluie():
    def __init__ (self,color,radius): 
        pygame.sprite.Sprite.__init__(self) #Nécessaire pour que python sache que c'est un sprite à afficher
        self.color = color
        self.radius = radius
        self.position_x = 0 
        self.position_y = 0

    def update(self): #Sert à mettre à jour/dessiner les particules
        pygame.draw.circle(screen, self.color, (self.position_x,self.position_y),self.radius)

    def random_position(self): #Sert à donner un mouvement aléatoire aux particules
        self.position_x += random.randint(0,600)

    def gravity(self):
        self.position_y -= 5

    def life(self): #Va être utile pour réduire la taille des particules graduellement
        self.radius -= 0.05

pluie = []


running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    current_time = pygame.time.get_ticks() #Donne le temps en millisecondes depuis que la loop a été commencée
    if current_time > next_particle_time: #Compare les deux temps pour ajouter une particule périodiquement
        pluie.append(Pluie((0,0,255),random.randint(0,10))) #Ajoute une particule à la liste avec les valeurs choisies
        next_particle_time = current_time + 15

    for p in pluie[:]: #Crée des particules en les ajoutant dans une liste
        p.update()
        p.random_position() #Mouvement aléatoire des particules
        p.life() #Réduit la taille des particules
        p.gravity
        if p.radius < 1: #Supprime les particules qui sont plus petites que 1 pixel pour libérer la RAM
            pluie.remove(p)


    pygame.display.set_caption("El Fuego    FPS : "+"{:.2f}".format(clock.get_fps())) #Affiche le nom de la fenêtre, les FPS et le nombres de particules présentes 
    pygame.display.flip()   
pygame.quit()