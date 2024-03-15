import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import pymunk
from pymunk.pygame_util import DrawOptions
import math

# Set up Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Block on Slope Simulation")

# Set up Pymunk
space = pymunk.Space()
space.gravity = (0, 900)

# Set up Pygame drawing options
draw_options = DrawOptions(screen)

# Create ground
ground = pymunk.Segment(space.static_body, (0, 600), (800, 600), 5)
ground.friction = 1.0
space.add(ground)

# Create slope
slope_angle_degrees = 30
slope_angle_radians = math.radians(slope_angle_degrees)
slope_body = pymunk.Body(body_type=pymunk.Body.STATIC)
slope_shape = pymunk.Segment(slope_body, (0, 600), (800, 600 - 800 * math.sin(slope_angle_radians)), 5)
slope_shape.friction = 0.5
space.add(slope_body, slope_shape)

# Create block
block_mass = 10
block_size = (50, 50)
block_moment = pymunk.moment_for_box(block_mass, block_size)
block_body = pymunk.Body(block_mass, block_moment)
# Calculate block position on the slope
block_x = 0  # Start of the slope
block_y = 600 - 800 * math.sin(slope_angle_radians) - block_size[1]  # Place block at the bottom of the slope
block_body.position = (block_x, block_y)
block_shape = pymunk.Poly.create_box(block_body, block_size)
block_shape.friction = 1.0
space.add(block_body, block_shape)

# Simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Step simulation
    space.step(1 / 60)

    # Clear screen
    screen.fill(THECOLORS["white"])

    # Visualize changing slope angle
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        slope_angle_degrees += 1
    elif keys[K_DOWN]:
        slope_angle_degrees -= 1
    slope_angle_radians = math.radians(slope_angle_degrees)
    slope_shape.unsafe_set_endpoints((0, 600), (800, 600 - 800 * math.sin(slope_angle_radians)))

    # Draw space
    space.debug_draw(draw_options)

    # Update Pygame display
    pygame.display.flip()

    # Tick clock
    clock.tick(60)

# Clean up
pygame.quit()
