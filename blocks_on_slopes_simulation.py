import pygame
from pygame.locals import *
import math
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
FPS = 60
x_pos = 0
time = 20
slope_x = 0
slope_y = 600
rotation = 0
rotation_speed = 2
WHITE = (0,0,0)
BLACK = (255,255,255)
image_orig = pygame.Surface((3000,10))
image_orig.set_colorkey(WHITE)
image_orig.fill(BLACK)
image = image_orig.copy()
image.set_colorkey(WHITE)
slope = image.get_rect()
slope.centre = (1280//2, 720//2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                x_pos += 1280/(time*2)
            if event.key == K_LEFT:
                x_pos -= 1280/(time*2)
    old_centre = slope.center
    rotation = (rotation + rotation_speed) % 360
    new_image = pygame.transform.rotate(image_orig, rotation)
    slope = new_image.get_rect()
    slope.centre = old_centre
    window.fill('white')
    window.blit(new_image , slope)
    '''pygame.draw.rect(window,'black',pygame.Rect(0,675,1280,5))
    pygame.draw.rect(window, 'black', pygame.Rect(x_pos, 680, 40, 40)
    pygame.display.update()
    print(x_pos)'''
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()