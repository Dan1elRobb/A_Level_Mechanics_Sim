import pygame
import pymunk
import sys
import math

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Pymunk setup
space = pymunk.Space()
space.gravity = (0, -1000)  # A more realistic gravity

# Adjustable variables
mass = 10.0
friction_coefficient = 0.3
slope_angle = math.radians(30)  # Initial angle of the slope in radians

# Create block and slope
block_width, block_height = 50, 30
block_moment = pymunk.moment_for_box(mass, (block_width, block_height))
block_body = pymunk.Body(mass, block_moment)
block_body.position = (width // 2, height // 2)  # Initial position of the block
block_shape = pymunk.Poly.create_box(block_body, (block_width, block_height))
space.add(block_body, block_shape)

slope_length = 200
slope_body = pymunk.Body(body_type=pymunk.Body.STATIC)
slope_shape = pymunk.Segment(slope_body, (width // 2 - slope_length // 2, height // 2),
                             (width // 2 + slope_length // 2, height // 2), 5)
slope_shape.color = (255, 0, 0, 255)  # Red color for the slope
slope_body.angle = slope_angle
space.add(slope_body, slope_shape)

# Joint to make sure the block rests on the slope
pivot_joint = pymunk.PivotJoint(slope_body, block_body, (width // 2, height // 2))
space.add(pivot_joint)

# Slide joint to restrict rotation
slide_joint = pymunk.SlideJoint(slope_body, block_body, (width // 2, height // 2),
                                (width // 2, height // 2), 0, slope_length / 2)
space.add(slide_joint)

# Main simulation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update simulation
    space.step(1 / 60.0)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw block
    block_position = int(block_body.position.x), height - int(block_body.position.y)
    pygame.draw.rect(screen, (0, 0, 255), (block_position[0] - block_width // 2,
                                          block_position[1] - block_height // 2,
                                          block_width, block_height))

    # Draw slope
    slope_vertices = (int(slope_shape.a.x), height - int(slope_shape.a.y)), \
                     (int(slope_shape.b.x), height - int(slope_shape.b.y))
    pygame.draw.lines(screen, slope_shape.color, False, slope_vertices, int(slope_shape.radius))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
