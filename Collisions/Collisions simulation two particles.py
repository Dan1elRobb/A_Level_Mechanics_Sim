import pymunk
import pymunk.pygame_util
import pygame as pg
import math

# Initialize Pygame
pg.init()

# Constants
WINDOW_SIZE = (800, 600)

# Pygame setup
screen = pg.display.set_mode(WINDOW_SIZE)
clock = pg.time.Clock()

# Pymunk setup
space = pymunk.Space()
space.gravity = 0, 0  # No gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

class Particle:
    def __init__(self, mass, radius, position, velocity, color):
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1.0  # Initial coefficient of restitution
        self.shape.friction = 0.5
        self.body.velocity = velocity
        self.shape.color = color
        space.add(self.body, self.shape)

# Collision handler for detecting collisions between particles
def particle_collision_handler(arbiter, space, data):
    # Set a specific coefficient of restitution for the collision
    arbiter.elasticity = 0.1  # coefficeitn of restitution

    # Get the velocities before the collision
    v1_before = arbiter.shapes[0].body.velocity
    v2_before = arbiter.shapes[1].body.velocity

    # Perform elastic collision manually
    m1 = arbiter.shapes[0].body.mass
    m2 = arbiter.shapes[1].body.mass

    v1_after = ((m1 - m2) / (m1 + m2)) * v1_before + (2 * m2 / (m1 + m2)) * v2_before
    v2_after = (2 * m1 / (m1 + m2)) * v1_before + ((m2 - m1) / (m1 + m2)) * v2_before

    arbiter.shapes[0].body.velocity = v1_after
    arbiter.shapes[1].body.velocity = v2_after

    return True

# Create particles with variable masses and initial velocities
particle1 = Particle(mass=3, radius=20, position=(200, 300), velocity=(47, 0), color=(255, 0, 0))
particle2 = Particle(mass=6, radius=15, position=(600, 300), velocity=(-800, 0), color=(0, 0, 255))

# Add collision handler for particles
handler = space.add_collision_handler(0, 0)  # Collides with itself
handler.pre_solve = particle_collision_handler

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # Update the simulation
    space.step(dt)

    # Draw the simulation
    screen.fill((255, 255, 255))

    # Manually draw Pymunk shapes
    for shape in space.shapes:
        if isinstance(shape, pymunk.shapes.Circle):
            pg.draw.circle(screen, shape.color, (round(shape.body.position.x), round(WINDOW_SIZE[1] - shape.body.position.y)), int(shape.radius))

    # Update the Pygame display
    pg.display.flip()

pg.quit()
