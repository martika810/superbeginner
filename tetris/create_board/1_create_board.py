import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Tetromino')
    while True:
        DISPLAYSURF.fill((  0,   0,   0))
        pygame.display.update()
        checkForQuit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        pygame.quit()
        sys.exit() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

if __name__ == '__main__':
    main()



