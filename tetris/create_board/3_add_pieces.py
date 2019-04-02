import pygame, sys, random
from tetris.create_board.pieces import get_pieces, get_colors, get_light_colors
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
    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()
    while True:
        DISPLAYSURF.fill((  0,   0,   0))
        board = getBlankBoard()
        addToBoard(board,fallingPiece)
        drawBoard(board, DISPLAYSURF)
        pygame.display.update()
        checkForQuit()

def getNewPiece():
    PIECES = get_pieces() # return all tetris pieces
    COLORS = get_colors() # return all available colors
    TEMPLATE_WIDTH = 5
    # return a random new piece in a random rotation and color
    random_color = random.randint(0, len(COLORS)-1)
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': 0,
                'x': int(BOARDWIDTH / 2) - int(TEMPLATE_WIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random_color}
    return newPiece

def drawBox(display_surf, boxx, boxy, color, pixelx=None, pixely=None):
    # draw a single box (each tetromino piece has four boxes)
    # at xy coordinates on the board. Or, if pixelx & pixely
    # are specified, draw to the pixel coordinates stored in
    # pixelx & pixely (this is used for the "Next" piece).
    COLORS = get_colors()
    LIGHTCOLORS = get_light_colors()
    if color == '.':
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pygame.draw.rect(display_surf, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
    pygame.draw.rect(display_surf, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))

def convertToPixelCoords(boxx, boxy):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))

def drawBoard(board, display_surf):
    # draw the border around the board
    pygame.draw.rect(display_surf, BLUE, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    # fill the background of the board
    pygame.draw.rect(display_surf, (0,0,0), (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    # draw the individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(display_surf, x, y, board[x][y])

def addToBoard(board, piece):
    PIECES = get_pieces() # return all tetris pieces
    TEMPLATE_WIDTH = TEMPLATE_HEIGHT = 5
    BLANK = '.'
    # fill in the board based on piece's location, shape, and rotation
    for x in range(TEMPLATE_WIDTH):
        for y in range(TEMPLATE_HEIGHT):
            if  PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

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



