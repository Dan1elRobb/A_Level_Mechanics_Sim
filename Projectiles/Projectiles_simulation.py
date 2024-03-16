"""
This module handles the creation and display of the projectiles' simulation. Uses the imported pymunk and pygame
 modules to create the particle and handle its' physics.
"""
import pymunk
import pymunk.pygame_util
import pygame as pg
import math
from graphs_or_exit_projectiles import graphs_or_rerun


def run_proj_sim():
    """
    This function allows this simulation module to be run by the main program
    """
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

    # Constants, adjust window height based on initial velocity of the particle
    if user_initial_vel <= 40:
        WINDOW_SIZE = (400, 75)
    elif user_initial_vel > 40 and user_initial_vel <= 100:
        WINDOW_SIZE = (1000, 300)
    elif user_initial_vel > 100 and user_initial_vel <= 200:
        WINDOW_SIZE = (1200, 500)
    elif user_initial_vel > 200:
        WINDOW_SIZE = (1200, 700)
    GRAVITY = 9.8  # Real-world gravity in meters per second squared

    # Pygame setup
    screen = pg.display.set_mode(WINDOW_SIZE)
    clock = pg.time.Clock()

    # Pymunk setup
    space = pymunk.Space()
    space.gravity = 0, -GRAVITY  # Gravity points downwards
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    class Projectile:
        """
        This class is used to define the projectile that is used in the projectiles question type

        Attributes
        ----------
        mass - the mass of the projectile
        angle - the angle of projection of the projectile
        initial_velocity - the initial velocity of the projectile
        start_height - the starting height of projection of the projectile

        Methods
        -------
        update - updates the position of the particle using the underlying physics module - pymunk
        draw - draws the particle to the screen at the correct position

        """
        def __init__(self, mass, angle, start_height, initial_velocity):
            """
            Define the parameters for a general projectile that the user can pick the mass,velocity and starting height
            of
            Parameters
            ----------
            mass
            angle
            initial_velocity
            start_height
            """
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
            """
            This method is used to progress the space of the physics simulation by a time period determined
            by the frames in the main loop
            Parameters
            ----------
            dt
            """
            # Update the physics simulation
            if not paused:
                space.step(dt)

                # Store the current position in the list
                self.previous_positions.append((self.body.position.x, WINDOW_SIZE[1] - self.body.position.y))

        def draw(self):
            """
            This method is used to draw the projectile to the screen at each loop of the game loop at correct positions
            """
            # Draw the projectile with inverted y-coordinate
            pg.draw.circle(screen, (255, 0, 0), (int(self.body.position.x), int(WINDOW_SIZE[1] - self.body.position.y)),
                           2)

            # Draw dotted line
            for i in range(1, len(self.previous_positions), 10):  # Increased the step to make the line more dotted
                pg.draw.line(screen, (0, 0, 0), self.previous_positions[i - 1], self.previous_positions[i], 2)

    # Add a static floor
    floor_static = space.static_body
    floor_segment = pymunk.Segment(floor_static, (0, 10), (WINDOW_SIZE[0] + 10, 10), 1)
    floor_segment.elasticity = 0.8
    floor_segment.friction = 0.5
    space.add(floor_segment)

    # Simulation setup
    projectile = Projectile(mass, angle, start_height + 10, initial_velocity)

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
