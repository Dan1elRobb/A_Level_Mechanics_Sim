import pymunk
import pymunk.pygame_util
import pygame as pg
import math


def run_bons_sim():
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
    SLOPE_WIDTH = 1280  # Set the initial window width
    SLOPE_HEIGHT = SLOPE_WIDTH * math.tan(math.radians(ANGLE))  # Calculate the slope height
    MAX_WINDOW_HEIGHT = 1000  # Set a maximum window height
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
        def __init__(self):
            pg.init()
            self.screen = pg.display.set_mode(WINDOW_SIZE)
            self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
            self.running = True
            self.paused = False

            # Moved the block creation outside the while loop to avoid creating a new block every frame
            self.block_body = pymunk.Body(mass=user_mass, moment=7)
            self.block_body.position = SLOPE_WIDTH - 10, WINDOW_HEIGHT - SLOPE_HEIGHT
            self.block = pymunk.Poly.create_box(self.block_body, (50, 50))
            self.block.friction = 1
            space.add(self.block_body, self.block, slope_segment)

        def run(self):
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

                pg.display.update()

            # Removed space.remove as it's not necessary, the space will be cleared when the program exits
            pg.quit()

    Sim().run()
