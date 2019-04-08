import pygame, sys
from pygame.locals import QUIT

YELLOW = (255, 212,30)
BLACK = (0,0,0)
GREEN = (49,153,6)
SCREEN_CENTER = (350,350)
PACMAN_RADIUS = 250
TOP_RIGHT_CORNER = (700,0)
BOTTOM_RIGHT_CORNER = (700,700)

def draw_pacman(screen):

    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, SCREEN_CENTER, PACMAN_RADIUS)
    pygame.draw.polygon(screen, BLACK, [SCREEN_CENTER, TOP_RIGHT_CORNER, BOTTOM_RIGHT_CORNER])
    pygame.draw.circle(screen,BLACK,(350, 175), 20)
    pygame.draw.circle(screen,GREEN,(350+87, 350), 20)
    pygame.draw.circle(screen,GREEN,(350+87*2, 350), 20)
    pygame.draw.circle(screen,GREEN,(350+87*3, 350), 20)

def display_pacman():
    pygame.init()
    screen = pygame.display.set_mode((700,700))

    while(True):
        draw_pacman(screen)
        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

display_pacman()