import pymunk
import pymunk.pygame_util
import pygame as pg
import math

# Initialize Pygame
pg.init()

# Constants
WINDOW_SIZE = (800, 600)
GRAVITY = 9.8  # Real-world gravity in meters per second squared

# Zoom factor
ZOOM_FACTOR = 2.0  # Increase this value to zoom in

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
        speed = 2 * initial_velocity  # Multiply by 2 to double the speed
        angle_radians = math.radians(angle)
        self.body.velocity = speed * math.cos(angle_radians), speed * math.sin(angle_radians)

        # List to store previous positions for dotted line
        self.previous_positions = []

    def update(self, dt):
        # Update the physics simulation
        space.step(dt)

        # Store the current position in the list
        self.previous_positions.append((self.body.position.x, WINDOW_SIZE[1] - self.body.position.y))

    def draw(self):
        # Draw the projectile with inverted y-coordinate
        pg.draw.circle(screen, (255, 0, 0), (int(self.body.position.x), int(WINDOW_SIZE[1] - self.body.position.y)), 5)

        # Draw dotted line
        for i in range(1, len(self.previous_positions), 5):  # Increased the step to make the line more dotted
            pg.draw.line(screen, (0, 0, 0, 128), self.previous_positions[i - 1], self.previous_positions[i], 2)


# Add a static floor
floor_static = space.static_body
floor_segment = pymunk.Segment(floor_static, (0, 10), (WINDOW_SIZE[0], 10), 4)
floor_segment.elasticity = 0.8
floor_segment.friction = 0.5
space.add(floor_segment)

# Add a static vertical line with the height written on it
height_line = pymunk.Segment(floor_static, (WINDOW_SIZE[0] // 2, 0), (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]), 2)
space.add(height_line)

# Simulation setup
mass = 10
angle = 30  # Initial angle in degrees
start_height = 300
initial_velocity = 15  # Adjust the initial speed as needed
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

    # Calculate the zoomed area based on the projectile's position
    zoomed_x = max(0, min(projectile.body.position.x - WINDOW_SIZE[0] / (2 * ZOOM_FACTOR), WINDOW_SIZE[0] * (1 - 1 / ZOOM_FACTOR)))
    zoomed_y = max(0, min(WINDOW_SIZE[1] - projectile.body.position.y - WINDOW_SIZE[1] / (2 * ZOOM_FACTOR), WINDOW_SIZE[1] * (1 - 1 / ZOOM_FACTOR)))

    # Apply zoom transformation
    zoomed_surface = pg.Surface((WINDOW_SIZE[0] * ZOOM_FACTOR, WINDOW_SIZE[1] * ZOOM_FACTOR))
    zoomed_surface.set_colorkey((0, 0, 0))
    zoomed_surface.blit(screen, (0, 0), (zoomed_x, zoomed_y, WINDOW_SIZE[0], WINDOW_SIZE[1]))

    # Manually draw Pymunk shapes on the zoomed surface
    for shape in space.shapes:
        if isinstance(shape, pymunk.shapes.Circle) and shape.body == projectile.body:
            pg.draw.circle(zoomed_surface, (255, 0, 0),
                           (round((shape.body.position.x - zoomed_x) * ZOOM_FACTOR),
                            round((WINDOW_SIZE[1] - shape.body.position.y + zoomed_y) * ZOOM_FACTOR)),
                           int(shape.radius * ZOOM_FACTOR))
        elif isinstance(shape, pymunk.shapes.Segment) and shape.body == floor_static:
            pg.draw.line(zoomed_surface, (0, 0, 0),
                         (round((shape.a.x - zoomed_x) * ZOOM_FACTOR),
                          round((WINDOW_SIZE[1] - shape.a.y + zoomed_y) * ZOOM_FACTOR)),
                         (round((shape.b.x - zoomed_x) * ZOOM_FACTOR),
                          round((WINDOW_SIZE[1] - shape.b.y + zoomed_y) * ZOOM_FACTOR)),
                         round(shape.radius * 2 * ZOOM_FACTOR))

    # Draw the dotted line on the zoomed surface
    for i in range(1, len(projectile.previous_positions), 5):  # Increased the step to make the line more dotted
        pg.draw.line(zoomed_surface, (0, 0, 0, 128),
                     (round((projectile.previous_positions[i - 1][0] - zoomed_x) * ZOOM_FACTOR),
                      round((WINDOW_SIZE[1] - projectile.previous_positions[i - 1][1] + zoomed_y) * ZOOM_FACTOR)),
                     (round((projectile.previous_positions[i][0] - zoomed_x) * ZOOM_FACTOR),
                      round((WINDOW_SIZE[1] - projectile.previous_positions[i][1] + zoomed_y) * ZOOM_FACTOR)),
                     2)

    # Draw the zoomed surface on the original screen
    screen.blit(pg.transform.scale(zoomed_surface, WINDOW_SIZE), (0, 0))

    # Draw the static vertical line with transparency
    pg.draw.line(screen, (0, 0, 0, 128), (WINDOW_SIZE[0] // 2, 0), (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]), 2)

    # Draw the height on the static vertical line
    font = pg.font.Font(None, 36)
    height_text = font.render(str(WINDOW_SIZE[1]), True, (0, 0, 0))
    screen.blit(height_text, (WINDOW_SIZE[0] // 2 - 20, WINDOW_SIZE[1] // 2))

    # Update the Pygame display
    pg.display.flip()

pg.quit()
