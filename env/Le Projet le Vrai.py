import pygame, random

# -- Variables --

pygame.init()
clock = pygame.time.Clock()
fps_limit = 60.0

resx = 626 #Dimensions of the window, aspect ratio of 16/9
resy = 563
screen = pygame.display.set_mode([resx,resy]) #Defines the window's size, here 1600x900 pixels

next_particle_time = 0

background_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\background_image_no_clouds.jpg')

# -- Classes --

class Particle():
    def __init__ (self,color,radius):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.radius = radius
        self.position_x = 313 
        self.position_y = 415

    def update(self):
        pygame.draw.circle(screen, self.color, (self.position_x,self.position_y),self.radius)

    def random_movement(self):
        self.position_x += random.randint(-2,2)
        self.position_y -= random.randint(0,1)

    def life(self):
        self.radius -= 0.05



cloud_image_1 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud1.png')
cloud_image_2 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud2.png')
cloud_image_3 = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\cloud3.png')

class Cloud1():
    def __init__(self,x,y):
        self.position_x = x
        self.position_y = y
        screen.blit(cloud_image_1,(x,y))

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


firecamp_image = pygame.image.load(r'C:\Users\yannd\OneDrive\Projet Pygame Informatique OC 2021\env\firecamp.png')

class Firecamp():
    def __init__(self):
        screen.blit(firecamp_image,(250,413))



# -- Objets --

# -- Listes --

particles = []

# -- Game loop --

running = True
while running:
    clock.tick(fps_limit) #Limite le nombre d'images par seconde du jeu à 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill((0,0,0))
    screen.blit(background_image, [0, 0])
    random_color = (255,random.randint(0,180),0)

    current_time = pygame.time.get_ticks()
    if current_time > next_particle_time:
        particles.append(Particle(random_color,random.randint(0,10)))
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