import pygame, sys
from pygame.locals import *
BLUE        = (  0,   0, 155)
BOX_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
X_MARGIN = int((SCREEN_WIDTH - BOARD_WIDTH * BOX_SIZE) / 2)
TOP_MARGIN = SCREEN_HEIGHT - (BOARD_HEIGHT * BOX_SIZE) - 5
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetromino')
    while True:
        screen.fill((  0,   0,   0))

        pygame.draw.rect(screen, BLUE, (X_MARGIN - 3, TOP_MARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
        game_matrix = create_game_matrix()
        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

def create_game_matrix():
    game_matrix_columns = 10
    game_matrix_rows = 20
    board = []
    for column in range(game_matrix_columns):
        column = []
        for row in range(game_matrix_rows):
            column.append('.')
        board.append(column)
    return board

if __name__ == '__main__':
    main()



