import pygame
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
FPS = 60
x_pos = 0
time = 20
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                x_pos += 1280/(time*2)
            if event.key == K_LEFT:
                x_pos -= 1280/(time*2)

    window.fill('white')
    pygame.draw.rect(window, 'black', pygame.Rect(x_pos, 680, 40, 40))
    pygame.display.update()
    print(x_pos)
    clock.tick(FPS)
pygame.quit()
