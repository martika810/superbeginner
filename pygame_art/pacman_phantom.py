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

def draw_phantom(screen):

    screen.fill(BLACK)
    pygame.draw.circle(screen, BLUE, SCREEN_CENTER, PACMAN_RADIUS)
    pygame.draw.rect(screen, BLUE, [150, 350, 400,250])
    pygame.draw.polygon(screen, BLUE, [(150,650),(225,600),(150,600)])
    pygame.draw.polygon(screen, BLUE, [(225,600),(288,650),(350,600)])
    pygame.draw.polygon(screen, BLUE, [(350,600),(412,650),(462,600)])
    pygame.draw.polygon(screen, BLUE, [(462,600),(550,650),(550,600)])
    # Eyes
    pygame.draw.circle(screen, WHITE, (350+125,350), 50)
    pygame.draw.circle(screen, WHITE, (350-50,350), 50)
    pygame.draw.circle(screen, DARK_BLUE, (350+125+25,350), 25)
    pygame.draw.circle(screen, DARK_BLUE, (350-50+25,350), 25)


def display_phantom():
    pygame.init()
    screen = pygame.display.set_mode((700,700))

    while(True):
        draw_phantom(screen)
        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

display_phantom()