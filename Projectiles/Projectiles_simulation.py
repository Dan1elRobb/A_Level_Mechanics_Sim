import pymunk
import pymunk.pygame_util
import pygame as pg
import math

# Initialize Pygame
pg.init()
with open('PVars.txt', "r") as file:
    # Read each line and assign values to variables
    user_angle = int(file.readline().strip())
    user_mass = int(file.readline().strip())
    user_initial_vel = int(file.readline().strip())
    user_starting_height = int(file.readline().strip())
    user_end_time = int(file.readline().strip())
# Simulation setup
mass = user_mass
angle = user_angle  # Initial angle in degrees
start_height = user_starting_height
initial_velocity = user_initial_vel  # Adjust the initial speed as needed


def calc_variables_over_time(angle, end_time, initial_vel, initial_height):
    t = 0
    time_list = []
    y_dis_list = []
    x_dis_list = []
    y_vel_list = []
    while t < end_time:
        y_s = initial_vel * math.sin(math.radians(angle)) * t - 4.9 * t ** 2 + initial_height
        x_s = initial_vel * math.cos(math.radians(angle)) * t
        y_vel = initial_vel * math.sin(math.radians(angle)) - 9.8 * t
        y_dis_list.append(abs(y_s))
        x_dis_list.append(x_s)
        y_vel_list.append(y_vel)
        time_list.append(t)
        t += 0.01
    return time_list, y_dis_list, x_dis_list, y_vel_list


def find_index_of_second_zero_displacement(dis_list):
    a = [i for i, n in enumerate(dis_list) if n < 3]
    return a[1]


index_of_second_zero_displacement = find_index_of_second_zero_displacement(
    calc_variables_over_time(user_angle, user_end_time, user_initial_vel, user_starting_height)[1])
# Constants
WINDOW_SIZE = (max(500,max(calc_variables_over_time(user_angle,user_end_time,user_initial_vel,user_starting_height)[2])), max(50, max(calc_variables_over_time(user_angle, user_end_time, user_initial_vel, user_starting_height)[1][0:index_of_second_zero_displacement])+25))
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
        self.body.position = 10, start_height
        self.shape = pymunk.Circle(self.body, 5)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        space.add(self.body, self.shape)

        # Set the initial velocity based on angle and user-defined initial_velocity
        speed = initial_velocity
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
        for i in range(1, len(self.previous_positions), 10):  # Increased the step to make the line more dotted
            pg.draw.line(screen, (0, 0, 0), self.previous_positions[i - 1], self.previous_positions[i], 2)


# Add a static floor
floor_static = space.static_body
floor_segment = pymunk.Segment(floor_static, (0, 10), (WINDOW_SIZE[0], 10), 4)
floor_segment.elasticity = 0.8
floor_segment.friction = 0.5
space.add(floor_segment)

# Simulation setup
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
    for shape in space.shapes:
        if isinstance(shape, pymunk.shapes.Circle) and shape.body == projectile.body:
            pg.draw.circle(screen, (255, 0, 0),
                           (round(shape.body.position.x), round(WINDOW_SIZE[1] - shape.body.position.y)),
                           int(shape.radius))
        elif isinstance(shape, pymunk.shapes.Segment) and shape.body == floor_static:
            pg.draw.line(screen, (0, 0, 0), (round(shape.a.x), round(WINDOW_SIZE[1] - shape.a.y)),
                         (round(shape.b.x), round(WINDOW_SIZE[1] - shape.b.y)), round(shape.radius * 2))

    pg.draw.line(screen, (0, 0, 255), (projectile.body.position.x, WINDOW_SIZE[1]),
                 (projectile.body.position.x, WINDOW_SIZE[1] - projectile.body.position.y), 2)

    # Draw the dotted line
    projectile.draw()

    # Draw the height on the static vertical line
    font = pg.font.Font(None, 36)
    height_text = font.render(str(WINDOW_SIZE[1]), True, (0, 0, 0))
    screen.blit(height_text, (WINDOW_SIZE[0] // 2 - 20, WINDOW_SIZE[1] // 2))

    # Draw the static vertical line with transparency
    pg.draw.line(screen, (0, 0, 0, 30), (WINDOW_SIZE[0] // 2, 0), (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]), 2)

    # Update the Pygame display
    pg.display.flip()

pg.quit()
