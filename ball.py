import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background_color = (0, 0, 0) # Black background color
sprite_color = (0, 20, 255)   # Blue sprite color
sprite_color2 = (255, 0, 0)   # Blue sprite color
x = 10
y = 15
a = 50
b = 55
ball_width = 20.
ball_height = 20.
x_speed = 5
y_speed = 5
a_speed = 5
b_speed = 5
clock = pygame.time.Clock()  # Create a clock for contorlling frame rate
frame_rate = 60              # Number of frames per second
while not pygame.event.get(QUIT):
    screen.fill(background_color)
    pygame.draw.ellipse(screen, sprite_color, (x, y, ball_width, ball_height))
    pygame.draw.ellipse(screen, sprite_color2, (a, b, ball_width, ball_height))
    b_speed += .5
    b += b_speed
    a += a_speed
    x += x_speed 
    y_speed += .5
    y += y_speed               # Reverse movement
    if x > 620. or x < 0:
        x_speed = -x_speed
    if y > 460. or y < 0:
        y_speed = -y_speed
    if a > 620. or a < 0:
        a_speed = -a_speed
    if b > 460. or b < 0:
        b_speed = -b_speed
    pygame.display.update()
    clock.tick(frame_rate)       #Limit frame rate
exit()
