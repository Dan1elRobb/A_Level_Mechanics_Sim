import pymunk
import pymunk.pygame_util
import pygame as pg
from graphs_or_exit_ctp import ctp_graphs_or_exit

def run_collision_two_particles():
    # Initialize Pygame
    with open('CTPVars.txt', "r") as file:
        # Read each line and assign values to variables
        user_mass_particle_one = float(file.readline().strip())
        user_mass_particle_two = float(file.readline().strip())
        user_vel_particle_one = float(file.readline().strip())
        user_vel_particle_two = float(file.readline().strip())
        user_coefficient_of_restitution = float(file.readline().strip())
        user_end_time = float(file.readline().strip())

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

        def set_vels(self, x, y):
            self.body.velocity = (x, y)

        def get_state(self):
            return self.body.position, self.body.velocity

        def set_state(self, position, velocity):
            self.body.position = position
            self.body.velocity = velocity

        def get_velocity(self):
            return self.body.velocity

    # Collision handler for detecting collisions between particles
    def particle_collision_handler(arbiter, space, data):
        # Set a specific coefficient of restitution for the collision
        arbiter.elasticity = user_coefficient_of_restitution  # coefficient of restitution

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
    particle1 = Particle(mass=user_mass_particle_one, radius=20, position=(200, 300),
                         velocity=(user_vel_particle_one, 0), color=(255, 0, 0))
    particle2 = Particle(mass=user_mass_particle_two, radius=15, position=(600, 300),
                         velocity=(-user_vel_particle_two, 0), color=(0, 0, 255))

    # Add collision handler for particles
    handler = space.add_collision_handler(0, 0)  # Collides with itself
    handler.pre_solve = particle_collision_handler

    running = True
    paused = False
    end_time = pg.time.get_ticks() + int(user_end_time * 1000)  # Convert seconds to milliseconds
    velocities_particle1 = []
    velocities_particle2 = []
    last_record_time = pg.time.get_ticks()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if paused:
                        paused = False
                        particle1.set_state(particle1_saved_state[0], particle1_saved_state[1])
                        particle2.set_state(particle2_saved_state[0], particle2_saved_state[1])
                    else:
                        paused = True
                        particle1_saved_state = particle1.get_state()
                        particle2_saved_state = particle2.get_state()

        if not paused:
            current_time = pg.time.get_ticks()
            if current_time > end_time:
                running = False

            dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

            # Update the simulation
            space.step(dt)

            # Record velocities every 0.01 seconds
            if current_time - last_record_time >= 10:  # 10 milliseconds (0.01 second)
                velocities_particle1.append(particle1.get_velocity())
                velocities_particle2.append(particle2.get_velocity())
                last_record_time = current_time

            # Draw the simulation
            screen.fill((255, 255, 255))

            # Manually draw Pymunk shapes
            for shape in space.shapes:
                if isinstance(shape, pymunk.shapes.Circle):
                    pg.draw.circle(screen, shape.color,
                                   (round(shape.body.position.x), round(WINDOW_SIZE[1] - shape.body.position.y)),
                                   int(shape.radius))

            # Update the Pygame display
            pg.display.flip()
    with open('CTP1_vels.txt','w') as f:
        for vel in velocities_particle1:
            f.write(str(vel[0])+'\n')
    with open('CTP2_vels.txt','w') as f:
        for vel in velocities_particle2:
            f.write(str(vel[0])+'\n')

    pg.quit()
    ctp_graphs_or_exit()


