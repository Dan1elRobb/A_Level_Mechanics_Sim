'''
This module is used to simulate the collision question type with only one particle and a wall
it involves the use of the graphs_or_exit_cwp module in order to seamlessly bring in the next GUI
for the user without delay

'''
import pymunk
import pymunk.pygame_util
import pygame as pg
from graphs_or_exit_cwp import cwp_graphs_or_exit


def run_collissions_wall_sim():
    """
    This function allows this simulation module to be run by the main program
    """
    with open('CWPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle = float(file.readline().strip())
        user_vel_particle = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())
    # Initialize Pygame
    pg.init()

    # Constants
    WINDOW_SIZE = (400, 300)

    # Pygame setup
    screen = pg.display.set_mode(WINDOW_SIZE)
    clock = pg.time.Clock()

    # Pymunk setup
    space = pymunk.Space()
    space.gravity = 0, 0  # No gravity (2d collision)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    class Particle:
        """
        This class is used to define a particle that is used in the collisions particle and wall question type

        Attributes
        ----------
        mass - the mass of the particle
        radius - the radius of the particle
        velocity - the velocity of the particle
        position - the position of the particle
        colour - colour of the particle

        Methods
        -------
        set_vel - sets the x and y velocity of the particle
        unpause - 'unpauses' the simulation by setting the x and y velocities to what they were pre pause
        get_velocity - returns the velocity of the particle

        """
        def __init__(self, mass, radius, position, velocity, colour):
            """
            Define the parameters for a general particle that the user can pick the mass and velocity of
            Allow for further customisation by defining colour and radius  of the particle though not allowing
            user to change them currently
            Parameters
            ----------
            mass
            radius
            position
            velocity
            colour
            """
            moment = pymunk.moment_for_circle(mass, 0, radius)
            self.body = pymunk.Body(mass, moment)
            self.body.position = position
            self.shape = pymunk.Circle(self.body, radius)
            self.shape.elasticity = 1.0  # Initial coefficient of restitution
            self.shape.friction = 0.5
            self.body.velocity = velocity
            self.shape.colour = colour
            space.add(self.body, self.shape)

        def set_vel(self, x, y):
            """
            Allows the program to edit the velocity of the particle using a method of the object
            Parameters
            ----------
            x
            y
            """
            self.body.velocity = (x, y)

        def unpause(self, velocity):
            self.body.velocity = velocity

        def get_velocity(self):
            """
            Allows the program to get the velocity of the particle using a method of the object
            Returns
            -------
            Velocity of the particle
            """
            return self.body.velocity

    # Collision handler for detecting collisions with the wall
    def wall_collision_handler(arbiter, space, data):
        # Set a specific coefficient of restitution for the collision with the wall
        arbiter.contacts[0].restitution = 0.8  # Adjust this value as needed

        # Get the velocity before the collision
        v_before = arbiter.shapes[0].body.velocity

        # Perform elastic collision manually with the wall
        v_after = (-1) * v_before  # Reverse the velocity component along the collision normal

        arbiter.shapes[0].body.velocity = v_after

        return True

    # Create particle with a variable mass and initial velocity
    particle = Particle(mass=user_mass_particle, radius=10, position=(350, 150), velocity=(user_vel_particle, 0),
                        colour=(255, 0, 0))

    # Create a wall (static segment) at the right side of the window
    wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    wall_segment = pymunk.Segment(wall_body, (WINDOW_SIZE[0], 0), (WINDOW_SIZE[0], WINDOW_SIZE[1]), 5)
    wall_segment.elasticity = user_coefficient_of_restitution  # Adjust this value as needed
    space.add(wall_body, wall_segment)

    # Add collision handler for particle-wall collisions
    handler = space.add_collision_handler(0, 1)
    handler.pre_solve = wall_collision_handler

    running = True
    paused = False
    end_time = pg.time.get_ticks() + int(user_end_time * 1000)  # Convert seconds to milliseconds
    velocities_particle = []
    last_record_time = pg.time.get_ticks()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if paused:
                        paused = False
                        particle.unpause(saved_velocity)
                    else:
                        paused = True
                        saved_velocity = particle.body.velocity
                        particle.set_vel(0, 0)

        current_time = pg.time.get_ticks()
        if current_time > end_time:
            running = False

        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

        # Update the simulation
        space.step(dt)

        # Draw the simulation
        screen.fill((255, 255, 255))
        # Record the velocity of the particle every 0.01 seconds (for the sake of graphs and outputs)
        if current_time - last_record_time >= 10:  # 10 milliseconds (0.01 second)
            velocities_particle.append(particle.get_velocity())
            last_record_time = current_time
        # Manually draw Pymunk shapes
        for shape in space.shapes:
            if isinstance(shape, pymunk.shapes.Circle):
                pg.draw.circle(screen, shape.colour,
                               (round(shape.body.position.x), round(WINDOW_SIZE[1] - shape.body.position.y)),
                               int(shape.radius))
            elif isinstance(shape, pymunk.shapes.Segment):
                pg.draw.line(screen, (0, 0, 0), (round(shape.a.x), round(WINDOW_SIZE[1] - shape.a.y)),
                             (round(shape.b.x), round(WINDOW_SIZE[1] - shape.b.y)), 5)

        # Update the Pygame display
        pg.display.flip()
    with open('CWP_vels.txt', 'w') as f:
        for velocity in velocities_particle:
            f.write(str(velocity[0]) + '\n')
    pg.quit()
    cwp_graphs_or_exit()
