#VERSION 1 : Création des particules qui vont servir à faire le feu

import pygame, random

# -- Variables --

pygame.init()
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 1600 #Dimensions of the window, aspect ratio of 16/9
resy = 900
screen = pygame.display.set_mode([resx,resy]) #Defines the window's size, here 1600x900 pixels

next_particle_time = 0



# -- Classes --

class Particle():
    def __init__ (self,color,radius):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.radius = radius
        self.position_x = random.randint(radius, 1600-radius)
        self.position_y = random.randint(radius, 900-radius)

    def update(self):
        pygame.draw.circle(screen, self.color, (self.position_x,self.position_y),self.radius)

    def random_movement(self):
        self.position_x += random.randint(0,5)
        self.position_y -= random.randint(0,5)

    def life(self):
        self.radius -= 1

# -- Objets --

particle1 = Particle((255,0,0),100)

# -- Lists --

particles = []

# -- Game loop --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    random_color = (255,random.randint(0,180),0)


    current_time = pygame.time.get_ticks()
    if current_time > next_particle_time:
        particles.append(Particle(random_color,random.randint(0,100)))
        next_particle_time = current_time + 10

    for p in particles[:]:
        p.update()
        p.random_movement()
        p.life()
        if p.radius < 1:
            particles.remove(p)
    print(len(particles))

    pygame.display.set_caption("Le feuf    FPS : "+"{:.2f}".format(clock.get_fps())+"    n Particules : "+str(len(particles)))
    #pygame.display.set_caption("{:.2f}".format(clock.get_fps()))

    pygame.display.flip()   
pygame.quit()