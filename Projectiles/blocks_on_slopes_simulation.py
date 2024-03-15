import pymunk
import pymunk.pygame_util
import pygame as pg
import math
from bons_exit_graphs import bons_graphs_or_exit

def run_bons_sim():
    # Open and read the text file in which the variables which the user inputted are stored and assign each a variable
    with open('BOSVars.txt', "r") as file:
        # Read each line and assign values to variables
        mass = float(file.readline().strip())
        angle = float(file.readline().strip())
        mew = float(file.readline().strip())
        end_time = float(file.readline().strip())

    # Initialise pygame
    pg.init()

    ANGLE = angle
    user_mass = mass
    user_mew = mew

    # Calculate the width based on the angle for a more appropriate window size
    SLOPE_WIDTH = 600  # Set the initial window width
    SLOPE_HEIGHT = SLOPE_WIDTH * math.tan(math.radians(ANGLE))  # Calculate the slope height
    MAX_WINDOW_HEIGHT = 700  # Set a maximum window height
    WINDOW_HEIGHT = min(int(SLOPE_HEIGHT) + 100, MAX_WINDOW_HEIGHT)  # Adjusted window height
    WINDOW_SIZE = (SLOPE_WIDTH, WINDOW_HEIGHT)  # Adjusted window size

    # Define colours
    BLACK = (255, 255, 255)

    # Allow Pymunk to draw to the pygame window
    draw_options = pymunk.pygame_util.DrawOptions(pg.display.set_mode(WINDOW_SIZE))

    # Create the pymunk space and assign it a gravity vector
    space = pymunk.Space()
    space.gravity = 0, 9.81

    # Create slope
    slope_static = space.static_body
    slope_segment = pymunk.Segment(slope_static, (0, WINDOW_HEIGHT),
                                   (SLOPE_WIDTH, WINDOW_HEIGHT - SLOPE_HEIGHT), 4)
    slope_segment.elasticity = 1
    slope_segment.friction = user_mew

    class Sim:
        '''
        This class is responsible for the blocks on slopes simulation
        '''
        def __init__(self):
            """
            Returns
            -------
            object

            """
            pg.init()
            self.screen = pg.display.set_mode(WINDOW_SIZE)
            self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
            self.running = True
            self.paused = False
            self.start_time = pg.time.get_ticks() / 1000  # Get start time in seconds
            self.max_sim_time = end_time  # Maximum simulation time

            # Calculate moment of inertia based on block's mass and size
            moment = pymunk.moment_for_box(user_mass, (50, 50))

            # Moved the block creation outside the while loop to avoid creating a new block every frame
            self.block_body = pymunk.Body(mass=user_mass, moment=moment)
            self.block_body.position = SLOPE_WIDTH - 10, WINDOW_HEIGHT - SLOPE_HEIGHT
            self.block = pymunk.Poly.create_box(self.block_body, (50, 50))
            self.block.friction = user_mew
            space.add(self.block_body, self.block, slope_segment)

        def run(self):
            """
            The method of the simulation class which handles the 'game' loop of pygame and pymunk integrated
            together. It is called only once when the simulation begins as the while loop is inside of the run
            method
            Returns
            -------
            object
            """
            clock = pg.time.Clock()  # Create a pygame clock
            while self.running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.running = False
                        elif event.key == pg.K_SPACE:
                            self.paused = not self.paused

                if not self.paused:
                    # If not paused, progress the simulation
                    space.step(0.01)

                self.screen.fill((220, 220, 220))
                space.debug_draw(self.draw_options)

                # Check elapsed time and exit simulation if necessary
                current_time = pg.time.get_ticks() / 1000  # Get current time in seconds
                elapsed_time = current_time - self.start_time
                if elapsed_time >= self.max_sim_time:
                    self.running = False

                pg.display.update()
            # Exit pygame (close the simulation display)
            pg.quit()
            # Execute the module imported at the top that brings up the next pop up for user
            bons_graphs_or_exit()

    Sim().run()


