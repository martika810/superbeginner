import pygame, sys
from pygame.locals import QUIT

WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (120,206,249)
DARK_BLUE = (16, 64, 141)
SCREEN_CENTER = (350,350)
PACMAN_RADIUS = 200
TOP_RIGHT_CORNER = (700,0)
BOTTOM_RIGHT_CORNER = (700,700)

def draw_house(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height),
          (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)


def display_phantom():
    pygame.init()
    screen = pygame.display.set_mode((700,700))

    while(True):
        draw_house(50,400,100,100,screen, BLUE)
        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

display_phantom()