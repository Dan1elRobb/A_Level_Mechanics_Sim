import pygame
pygame.init()

# screen dimensions
width = 1000
height = 600
screen_res = (width, height)

# create display
pygame.display.set_caption("sim prototype")
screen = pygame.display.set_mode(screen_res)


red = (255, 0, 0)
black = (0, 0, 0)

# define ball
ball_obj = pygame.draw.circle(
    surface=screen, color=red, center=[100, 100], radius=40)
speed = [1, 1]
acc = 0.2
# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)

    # move the ball
    ball_obj = ball_obj.move(speed)
    print(f'Speed is {speed}')

    # flip vels if ball contacts edge of window and sims accel
    if ball_obj.left <= 0 or ball_obj.right >= width:
        if speed[0] > 0:
            speed[0] = -(speed[0] + acc)
        elif speed[0] < 1:
            speed[0] = -(speed[0] - acc)
    if ball_obj.top <= 0 or ball_obj.bottom >= height:
        if speed[1] > 0:
            speed[1] = -(speed[1] + acc)
        elif speed[1] < 1:
            speed[1] = -(speed[1] - acc)


    # draw ball at new centers that are obtained after moving
    pygame.draw.circle(surface=screen, color=red,
                       center=ball_obj.center, radius=40)

    pygame.display.flip()
