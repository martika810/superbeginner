
def get_colors():
    #               R    G    B
    WHITE       = (255, 255, 255)
    GRAY        = (185, 185, 185)
    BLACK       = (  0,   0,   0)
    RED         = (155,   0,   0)
    LIGHTRED    = (175,  20,  20)
    GREEN       = (  0, 155,   0)
    LIGHTGREEN  = ( 20, 175,  20)
    BLUE        = (  0,   0, 155)
    LIGHTBLUE   = ( 20,  20, 175)
    YELLOW      = (155, 155,   0)
    LIGHTYELLOW = (175, 175,  20)
    COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
    return COLORS

def get_light_colors():
    #               R    G    B
    WHITE       = (255, 255, 255)
    GRAY        = (185, 185, 185)
    BLACK       = (  0,   0,   0)
    RED         = (155,   0,   0)
    LIGHTRED    = (175,  20,  20)
    GREEN       = (  0, 155,   0)
    LIGHTGREEN  = ( 20, 175,  20)
    BLUE        = (  0,   0, 155)
    LIGHTBLUE   = ( 20,  20, 175)
    YELLOW      = (155, 155,   0)
    LIGHTYELLOW = (175, 175,  20)
    COLORS      = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
    return COLORS



def get_pieces():
    S_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '..OO.',
                         '.OO..',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..OO.',
                         '...O.',
                         '.....']]

    Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

    I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

    O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

    J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

    L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

    T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

    PIECES = {'S': S_SHAPE_TEMPLATE,
              'Z': Z_SHAPE_TEMPLATE,
              'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

    return PIECES