import pymunk
import pymunk.pygame_util
import pygame as pg
import math
# Initialise pygame
pg.init()
# Define window size as a constant and at create the pygame window
WINDOW_SIZE = (1280, 720)
window = pg.display.set_mode(WINDOW_SIZE)
ANGLE = 30
print(math.radians(ANGLE))

# Define colours
BLACK = (255, 255, 255)
# Allow Pymunk to draw to the pygame window
draw_options = pymunk.pygame_util.DrawOptions(window)

# Create the pymunk space and assign it a gravity vector
space = pymunk.Space()
space.gravity = 0, 100

# Create slope
SLOPE_Y_POS_BECAUSE_OF_ANGLE = 1280 * math.tan(math.radians((ANGLE)))
slope_static = space.static_body
slope_segment = pymunk.Segment(slope_static, (0, 720), (1280, SLOPE_Y_POS_BECAUSE_OF_ANGLE), 4)
slope_segment.elasticity = 1


# Create Block
block_body = pymunk.Body(mass=5, moment=10)
block_body.position = 1000, 20
block = pymunk.Poly.create_box(block_body, (50, 50))


# Add Block to space
space.add(block_body, block, slope_segment)


# Pygame event loop

class Sim:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WINDOW_SIZE)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill((220, 220, 220))
            space.debug_draw(self.draw_options)
            pg.display.update()
            space.step(0.01)

        pg.quit()


Sim().run()
