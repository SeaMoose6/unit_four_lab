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
def wave_animate(x, y):
    pygame.draw.arc(screen, WAVES, [x, y, 150, 150], 0, PI / 2, 10)
    pygame.draw.arc(screen, WAVES, [x, y, 130, 150], 0, PI / 2.5, 10)

    pygame.draw.arc(screen, WAVES, [x-12.5, y+12.5, 140, 125], 0, PI / 2.1, 10)
    pygame.draw.arc(screen, WAVES, [x-12.5, y+12.5, 120, 125], 0, PI / 2.6, 10)

    pygame.draw.arc(screen, WAVES, [x-25, y+25, 130, 100], 0, PI / 2.2, 10)
    pygame.draw.arc(screen, WAVES, [x-25, y+25, 110, 100], 0, PI / 2.7, 10)

    pygame.draw.arc(screen, WAVES, [x-37.5, y+37.5, 120, 75], 0, PI / 2.4, 10)
    pygame.draw.arc(screen, WAVES, [x-37.5, y+37.5, 100, 75], 0, PI / 2.8, 10)

    pygame.draw.arc(screen, WAVES, [x-50, y+50, 110, 50], 0, PI / 2.6, 10)
    pygame.draw.arc(screen, WAVES, [x-50, y+50, 90, 50], 0, PI / 2.9, 10)


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
    pygame.draw.rect(screen, UMBRELLA, [400, 50, 600, 170], 0)
    pygame.draw.arc(screen, SKY_BLUE, [400, 55, 600, 350], 0, PI, 20)
    pygame.draw.arc(screen, SKY_BLUE, [390, 45, 620, 360], 0, PI, 20)
    pygame.draw.arc(screen, SKY_BLUE, [370, 45, 660, 360], 0, PI, 20)
    pygame.draw.arc(screen, SKY_BLUE, [360, 45, 680, 360], 0, PI, 20)
    pygame.draw.arc(screen, SKY_BLUE, [350, 45, 700, 360], 0, PI, 20)
    pygame.draw.arc(screen, SKY_BLUE, [340, 35, 720, 360], 0, PI, 20)
    pygame.draw.polygon(screen, SKY_BLUE, [(400, 50), (600, 50), (400, 145)])
    pygame.draw.polygon(screen, SKY_BLUE, [(1000, 150), (800, 50), (1000, 50)])
    #pygame.draw.line(screen, UMBRELLA, (401, 215), (1000, 220), 10)


    # sun
    pygame.draw.circle(screen, SUN, (0, 0), 150)

    # towel
    pygame.draw.polygon(screen, TOWEL, [(200, 550), (150, 650), (450, 750), (500, 650)])

    #wave_animate(500, 600)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()