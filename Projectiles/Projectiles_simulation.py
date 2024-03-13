import pymunk
import pymunk.pygame_util
import pygame as pg
import math
from graphs_or_rerun_sim_projectiles import graphs_or_rerun
from Projectile_Variables_Outputs import run_proj_outputs
def run_proj_sim():
    # Initialize Pygame
    pg.init()
    with open('PVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_angle = float(file.readline().strip())
        user_mass = float(file.readline().strip())
        user_initial_vel = float(file.readline().strip())
        user_starting_height = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
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


    def find_index_of_second_zero_displacement_using25(dis_list):
        a = [i for i, n in enumerate(dis_list) if n < 25]
        return a[1]

    def find_index_of_second_zero_displacement_using10(dis_list):
        a = [i for i, n in enumerate(dis_list) if n < 15]
        return a[1]

    # Constants
    if user_initial_vel <= 40:
        WINDOW_SIZE = (400,75)
    elif user_initial_vel >40 and user_initial_vel <= 100:
        WINDOW_SIZE = (1000,300)
    elif user_initial_vel > 100 and user_initial_vel <= 200:
        WINDOW_SIZE = (1200,500)
    elif user_initial_vel > 200:
        WINDOW_SIZE = (1200,700)
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
            if not paused:
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
    floor_segment = pymunk.Segment(floor_static, (0, 10), (WINDOW_SIZE[0]+10, 10), 4)
    floor_segment.elasticity = 0.8
    floor_segment.friction = 0.5
    space.add(floor_segment)

    # Simulation setup
    projectile = Projectile(mass, angle, start_height, initial_velocity)

    running = True
    paused = False
    simulation_time = 0
    total_elapsed_time = 0
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                if event.key == pg.K_SPACE:
                    if paused:
                        pause_time = pg.time.get_ticks() / 1000.0  # Convert milliseconds to seconds
                        total_elapsed_time += (pause_time - simulation_time)
                    paused = not paused
        if not paused:
            dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

            # Update the simulation
            projectile.update(dt)

            simulation_time += dt

            if simulation_time >= user_end_time:
                running = False

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
        height_text = font.render(str(WINDOW_SIZE[1])[0:3], True, (0, 0, 0))
        screen.blit(height_text, (WINDOW_SIZE[0] // 2 - 20, WINDOW_SIZE[1] // 2))

        # Draw the static vertical line with transparency
        pg.draw.line(screen, (0, 0, 0, 30), (WINDOW_SIZE[0] // 2, 0), (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]), 2)

        # Update the Pygame display
        pg.display.flip()
    pg.quit()
    graphs_or_rerun()

