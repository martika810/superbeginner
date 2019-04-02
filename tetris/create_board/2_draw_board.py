import pygame, sys
from pygame.locals import *
BLUE        = (  0,   0, 155)
BOXSIZE = 20
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOARDWIDTH = 10
BOARDHEIGHT = 20
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5
def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Tetromino')
    while True:
        DISPLAYSURF.fill((  0,   0,   0))
        board = getBlankBoard()
        drawBoard(DISPLAYSURF)
        pygame.display.update()
        checkForQuit()

def drawBoard(display_surf):
    # draw the border around the board
    pygame.draw.rect(display_surf, BLUE, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    # fill the background of the board
    pygame.draw.rect(display_surf, (0,0,0), (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))

def getBlankBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(10):
        board.append(['.'] * 20)
    return board

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



