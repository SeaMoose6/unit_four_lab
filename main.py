import pygame
import math

pygame.init()

#constants
SKY_BLUE = (53, 171, 184)
SAND = (201, 146, 50)
UMBRELLA = (201, 48, 34)
WHITE = (255, 255, 255)
OCEAN = (32, 98, 179)
BLACK = (0, 0, 0)
SUN = (255, 187, 0)
WAVES = (4, 52, 110)
TOWEL = (255, 145, 217)

PI = math.pi

SIZE = (1000, 750)
FPS = 60

# functions
def wave_right(x, y):
    pygame.draw.arc(screen, WAVES, [x, y, 150, 150], 0, PI/2, 10)
    pygame.draw.arc(screen, WAVES, [x, y, 130, 150], 0, PI/2.5, 10)
def wave_left(x, y):
    pygame.draw.arc(screen, WAVES, [x, y, 150, 150], PI/2, PI, 10)
    pygame.draw.arc(screen, WAVES, [x+300, y-5, 150, 155], PI/1.6, PI, 10)
    # pygame.draw.polygon(screen, OCEAN, [(x+75, y+100), (x+130, y+75), (x+200, y+100)])


pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("The Beach")

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY_BLUE)
    # waves
    pygame.draw.rect(screen, OCEAN, [0, 300, 1000, 1000])
    for num in range(10):
        wave_right(num*90, 250)
    for num in range(-5, 10):
        wave_left(num*90, 350)
    for num in range(10):
        wave_right(num*90, 450)

    # beach
    pygame.draw.rect(screen, SAND, [0, 600, 1000, 1000])
    pygame.draw.arc(screen, SAND, [-50, 500, 300, 700], 0, 180, 250)
    pygame.draw.arc(screen, SAND, [0, 500, 500, 700], 0, 180, 250)
    pygame.draw.arc(screen, SAND, [100, 500, 600, 700], 0, 180, 250)
    pygame.draw.arc(screen, SAND, [200, 550, 700, 700], 0, 180, 250)
    pygame.draw.arc(screen, SAND, [700, 500, 500, 700], 0, 180, 2250)


    # umbrella
    pygame.draw.line(screen, BLACK, (650, 600), (700, 150), 10)
    pygame.draw.arc(screen, UMBRELLA, [400, 50, 600, 350], 0, PI, 10)
    pygame.draw.line(screen, UMBRELLA, (401, 215), (1000, 220), 10)


    # sun
    pygame.draw.circle(screen, SUN, (0, 0), 150)

    # towel
    pygame.draw.polygon(screen, TOWEL, [(200, 550), (150, 650), (450, 750), (500, 650)])


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()