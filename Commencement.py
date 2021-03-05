import pygame
pygame.init()

screen = pygame.display.set_mode([800,800])

clock = pygame.time.Clock()
fps_limit = 60.0

posx = 400
posy = 400

running = True
while running:
    clock.tick(fps_limit)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    circle = pygame.draw.circle(screen, (255,0,0), (posx, posy), 100)
    pygame.display.flip()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            posx = posx - 10
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            posx = posx + 10
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            posy = posy - 10
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            posy = posy + 10
    
pygame.quit()