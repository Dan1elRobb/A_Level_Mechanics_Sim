import pymunk
import pymunk.pygame_util
import pygame as pg


# Initialise pygame
pg.init()
# Define window size as a constant and at create the pygame window
WINDOW_SIZE = 1280, 720
window = pg.display.set_mode(WINDOW_SIZE)

# Define colours
BLACK = (255,255,255)
# Allow Pymunk to draw to the pygame window
draw_options = pymunk.pygame_util.DrawOptions(window)

# Create the pymunk space and assign it a gravity vector
space = pymunk.Space()
space.gravity = 0, -900

# Create slope
slope_static = space.static_body
slope_segment = pymunk.Segment(slope_static, (0,0), (WINDOW_SIZE[0],0), 4)
slope_segment.elasticity = 1

# Create Block
block_body = pymunk.Body(mass=1, moment=10)
block_body.position = 100, 200
block = pymunk.Circle(block_body, radius=20)
block.elasticity = 0.9

# Add Block to space
space.add(block_body, block, slope_segment)

# Pygame event loop

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    window.fill(BLACK)
    space.debug_draw(draw_options)
    pg.display.update()
    space.step(0.01)

pg.quit()




