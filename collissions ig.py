import sys, random
import pymunk
import pygame
import pymunk.pygame_util


def add_particle(space, mass):
    """Add a particle to the simulation"""
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass,inertia)
    body.position = 100,100
    shape = pymunk.Circle(body,radius,(0,0))
    shape.friction = 1
    space.add(body,shape)
    return shape

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("collissions")
    clock = pygame.time.Clock()