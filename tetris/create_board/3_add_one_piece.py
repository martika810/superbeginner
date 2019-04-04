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
def run_tetris_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetromino')
    game_matrix = create_game_matrix()
    while True:
        screen.fill((  0,   0,   0))

        pygame.draw.rect(screen, BLUE, (X_MARGIN - 3, TOP_MARGIN - 7, (BOARD_WIDTH * BOX_SIZE) + 8, (BOARD_HEIGHT * BOX_SIZE) + 8), 5)
        for col in range(BOARD_WIDTH):
            for row in range(BOARD_HEIGHT):
                if(game_matrix[row][col] != '.'):
                    pygame.draw.rect(screen, (255,255,255),9*20+X_MARGIN)

        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

def add_one_piece(board):
    board[9][1] = (255,255,255)


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


run_tetris_game()



