import pymunk
import pymunk.pygame_util
import pygame as pg
import math

# Initialize Pygame
pg.init()

# Constants
WINDOW_SIZE = (800, 600)
GRAVITY = 9.8  # Real-world gravity in meters per second squared

# Pygame setup
screen = pg.display.set_mode(WINDOW_SIZE)
clock = pg.time.Clock()

# Pymunk setup
space = pymunk.Space()
space.gravity = 0, -GRAVITY  # Gravity points downwards
draw_options = pymunk.pygame_util.DrawOptions(screen)


class Projectile:
    def __init__(self, mass, angle, start_height, initial_velocity):
        moment = pymunk.moment_for_circle(mass, 0, 5)
        self.body = pymunk.Body(mass, moment)
        self.body.position = 100, start_height
        self.shape = pymunk.Circle(self.body, 5)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        space.add(self.body, self.shape)

        # Set the initial velocity based on angle and user-defined initial_velocity
        speed = initial_velocity
        angle_radians = math.radians(angle)
        self.body.velocity = speed * math.cos(angle_radians), speed * math.sin(angle_radians)

    def update(self, dt):
        # Update the physics simulation
        space.step(dt)

    def draw(self):
        # Draw the projectile with inverted y-coordinate
        pg.draw.circle(screen, (255, 0, 0), (int(self.body.position.x), int(WINDOW_SIZE[1] - self.body.position.y)), 5)


# Add a static floor
floor_static = space.static_body
floor_segment = pymunk.Segment(floor_static, (0, 10), (WINDOW_SIZE[0], 10), 4)
floor_segment.elasticity = 0.8
floor_segment.friction = 0.5
space.add(floor_segment)

# Simulation setup
mass = 10
angle = 45  # Initial angle in degrees
start_height = 10
initial_velocity = 60  # Adjust the initial speed as needed
projectile = Projectile(mass, angle, start_height, initial_velocity)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # Update the simulation
    projectile.update(dt)

    # Draw the simulation
    screen.fill((255, 255, 255))

    # Manually draw Pymunk shapes
    # Manually draw Pymunk shapes
    for shape in space.shapes:
        if isinstance(shape, pymunk.shapes.Circle) and shape.body == projectile.body:
            pg.draw.circle(screen, (255, 0, 0),
                           (round(shape.body.position.x), round(WINDOW_SIZE[1] - shape.body.position.y)),
                           int(shape.radius))
        elif isinstance(shape, pymunk.shapes.Segment) and shape.body == floor_static:
            pg.draw.line(screen, (0, 0, 0), (round(shape.a.x), round(WINDOW_SIZE[1] - shape.a.y)),
                         (round(shape.b.x), round(WINDOW_SIZE[1] - shape.b.y)), round(shape.radius * 2))

    # Update the Pygame display
    pg.display.flip()

pg.quit()
