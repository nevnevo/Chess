import pygame

pygame.init()

screen = pygame.display.set_mode((800 , 800))


# Board
# every cell holds image
# holds piece from liam's class (every should hold )
# state is selected, is empty, is colored
# img

class Board:
    img = pygame.image.load(('Images/whitesquare.png'))
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i+j)%2 == 0:
                img = pygame.image.load('Images/whitesquare.png')
            else:
                img = pygame.image.load('Images/blacksquare.png')

            img = pygame.transform.scale(img, (100, 100))
            row.append(img)
        board.append(row)

    # all this code becomes the loop we defined within the squares.py file
    # black
    a2 = pygame.image.load('Images/whitesquare.png')
    a2 = pygame.transform.scale(a2, (100, 100))
    a4 = pygame.image.load('Images/whitesquare.png')
    a4 = pygame.transform.scale(a4, (100, 100))
    a6 = pygame.image.load('Images/whitesquare.png')
    a6 = pygame.transform.scale(a6, (100, 100))
    a8 = pygame.image.load('Images/whitesquare.png')
    a8 = pygame.transform.scale(a8, (100, 100))


    b1 = pygame.image.load('Images/whitesquare.png')
    b1 = pygame.transform.scale(b1, (100, 100))
    b3 = pygame.image.load('Images/whitesquare.png')
    b3 = pygame.transform.scale(b3, (100, 100))
    b5 = pygame.image.load('Images/whitesquare.png')
    b5 = pygame.transform.scale(b5, (100, 100))
    b7 = pygame.image.load('Images/whitesquare.png')
    b7 = pygame.transform.scale(b7, (100, 100))

    c2 = pygame.image.load('Images/whitesquare.png')
    c2 = pygame.transform.scale(c2, (100, 100))
    c4 = pygame.image.load('Images/whitesquare.png')
    c4 = pygame.transform.scale(c4, (100, 100))
    c6 = pygame.image.load('Images/whitesquare.png')
    c6 = pygame.transform.scale(c6, (100, 100))
    c8 = pygame.image.load('Images/whitesquare.png')
    c8 = pygame.transform.scale(c8, (100, 100))

    d1 = pygame.image.load('Images/whitesquare.png')
    d1 = pygame.transform.scale(b1, (100, 100))
    d3 = pygame.image.load('Images/whitesquare.png')
    d3 = pygame.transform.scale(b3, (100, 100))
    d5 = pygame.image.load('Images/whitesquare.png')
    d5 = pygame.transform.scale(b5, (100, 100))
    d7 = pygame.image.load('Images/whitesquare.png')
    d7 = pygame.transform.scale(b7, (100, 100))

    e2 = pygame.image.load('Images/whitesquare.png')
    e2 = pygame.transform.scale(a2, (100, 100))
    e4 = pygame.image.load('Images/whitesquare.png')
    e4 = pygame.transform.scale(a4, (100, 100))
    e6 = pygame.image.load('Images/whitesquare.png')
    e6 = pygame.transform.scale(a6, (100, 100))
    e8 = pygame.image.load('Images/whitesquare.png')
    e8 = pygame.transform.scale(a8, (100, 100))

    f1 = pygame.image.load('Images/whitesquare.png')
    f1 = pygame.transform.scale(b1, (100, 100))
    f3 = pygame.image.load('Images/whitesquare.png')
    f3 = pygame.transform.scale(b3, (100, 100))
    f5 = pygame.image.load('Images/whitesquare.png')
    f5 = pygame.transform.scale(b5, (100, 100))
    f7 = pygame.image.load('Images/whitesquare.png')
    f7 = pygame.transform.scale(b7, (100, 100))

    g2 = pygame.image.load('Images/whitesquare.png')
    g2 = pygame.transform.scale(a2, (100, 100))
    g4 = pygame.image.load('Images/whitesquare.png')
    g4 = pygame.transform.scale(a4, (100, 100))
    g6 = pygame.image.load('Images/whitesquare.png')
    g6 = pygame.transform.scale(a6, (100, 100))
    g8 = pygame.image.load('Images/whitesquare.png')
    g8 = pygame.transform.scale(a8, (100, 100))

    h1 = pygame.image.load('Images/whitesquare.png')
    h1 = pygame.transform.scale(b1, (100, 100))
    h3 = pygame.image.load('Images/whitesquare.png')
    h3 = pygame.transform.scale(b3, (100, 100))
    h5 = pygame.image.load('Images/whitesquare.png')
    h5 = pygame.transform.scale(b5, (100, 100))
    h7 = pygame.image.load('Images/whitesquare.png')
    h7 = pygame.transform.scale(b7, (100, 100))

    # white
    a1 = pygame.image.load('Images/blacksquare.png')
    a1 = pygame.transform.scale(a1, (100, 100))
    a3 = pygame.image.load('Images/blacksquare.png')
    a3 = pygame.transform.scale(a3, (100, 100))
    a5 = pygame.image.load('Images/blacksquare.png')
    a5 = pygame.transform.scale(a5, (100, 100))
    a7 = pygame.image.load('Images/blacksquare.png')
    a7 = pygame.transform.scale(a7, (100, 100))


    b2 = pygame.image.load('Images/blacksquare.png')
    b2 = pygame.transform.scale(b2, (100, 100))
    b4 = pygame.image.load('Images/blacksquare.png')
    b4 = pygame.transform.scale(b4, (100, 100))
    b6 = pygame.image.load('Images/blacksquare.png')
    b6 = pygame.transform.scale(b6, (100, 100))
    b8 = pygame.image.load('Images/blacksquare.png')
    b8 = pygame.transform.scale(b8, (100, 100))

    c1 = pygame.image.load('Images/blacksquare.png')
    c1 = pygame.transform.scale(c1, (100, 100))
    c3 = pygame.image.load('Images/blacksquare.png')
    c3 = pygame.transform.scale(c3, (100, 100))
    c5 = pygame.image.load('Images/blacksquare.png')
    c5 = pygame.transform.scale(c5, (100, 100))
    c7 = pygame.image.load('Images/blacksquare.png')
    c7 = pygame.transform.scale(c7, (100, 100))

    d2 = pygame.image.load('Images/blacksquare.png')
    d2 = pygame.transform.scale(b2, (100, 100))
    d4 = pygame.image.load('Images/blacksquare.png')
    d4 = pygame.transform.scale(b4, (100, 100))
    d6 = pygame.image.load('Images/blacksquare.png')
    d6 = pygame.transform.scale(b6, (100, 100))
    d8 = pygame.image.load('Images/blacksquare.png')
    d8 = pygame.transform.scale(b8, (100, 100))

    e1 = pygame.image.load('Images/blacksquare.png')
    e1 = pygame.transform.scale(a1, (100, 100))
    e3 = pygame.image.load('Images/blacksquare.png')
    e3 = pygame.transform.scale(a3, (100, 100))
    e5 = pygame.image.load('Images/blacksquare.png')
    e5 = pygame.transform.scale(a5, (100, 100))
    e7 = pygame.image.load('Images/blacksquare.png')
    e7 = pygame.transform.scale(a7, (100, 100))

    f2 = pygame.image.load('Images/blacksquare.png')
    f2 = pygame.transform.scale(b2, (100, 100))
    f4 = pygame.image.load('Images/blacksquare.png')
    f4 = pygame.transform.scale(b4, (100, 100))
    f6 = pygame.image.load('Images/blacksquare.png')
    f6 = pygame.transform.scale(b6, (100, 100))
    f8 = pygame.image.load('Images/blacksquare.png')
    f8 = pygame.transform.scale(b8, (100, 100))

    g1 = pygame.image.load('Images/blacksquare.png')
    g1 = pygame.transform.scale(a1, (100, 100))
    g3 = pygame.image.load('Images/blacksquare.png')
    g3 = pygame.transform.scale(a3, (100, 100))
    g5 = pygame.image.load('Images/blacksquare.png')
    g5 = pygame.transform.scale(a5, (100, 100))
    g7 = pygame.image.load('Images/blacksquare.png')
    g7 = pygame.transform.scale(a7, (100, 100))

    h2 = pygame.image.load('Images/blacksquare.png')
    h2 = pygame.transform.scale(b2, (100, 100))
    h4 = pygame.image.load('Images/blacksquare.png')
    h4 = pygame.transform.scale(b4, (100, 100))
    h6 = pygame.image.load('Images/blacksquare.png')
    h6 = pygame.transform.scale(b6, (100, 100))
    h8 = pygame.image.load('Images/blacksquare.png')
    h8 = pygame.transform.scale(b8, (100, 100))


#Configuring File lists

    A_file = [a1,a2,a3,a4,a5,a6,a7,a8]
    B_file = [b1,b2,b3,b4,b5,b6,b7,b8]
    C_file = [c1,c2,c3,c4,c5,c6,c7,c8]
    D_file = [d1,d2,d3,d4,d5,d6,d7,d8]
    E_file = [e1,e2,e3,e4,e5,e6,e7,e8]
    F_file = [f1,f2,f3,f4,f5,f6,f7,f8]
    G_file = [g1,g2,g3,g4,g5,g6,g7,g8]
    H_file = [h1,h2,h3,h4,h5,h6,h7,h8]

#Configuring Row Lists

    Row_1 = [a1, b1, c1, d1, e1, f1, g1, h1]
    Row_2 = [a2, b2, c2, d2, e2, f2, g2, h2]
    Row_3 = [a3, b3, c3, d3, e3, f3, g3, h3]
    Row_4 = [a4, b4, c4, d4, e4, f4, g4, h4]
    Row_5 = [a5, b5, c5, d5, e5, f5, g5, h5]
    Row_6 = [a6, b6, c6, d6, e6, f6, g6, h6]
    Row_7 = [a7, b7, c7, d7, e7, f7, g7, h7]
    Row_8 = [a8, b8, c8, d8, e8, f8, g8, h8]


#Configuring Diagnoals Lists

    Dia_1 = [g1,h2]
    Dia_2 = [e1,f2,g3, h4]
    Dia_3 = [c1,d2, e3, f4, g5, h6]
    Dia_4 = [a1,b2,c3, d4, e5, f6, g7, h8]
    Dia_5 = [a3, b4, c5, d6, e7, f8]
    Dia_6 = [a5, b6, c7, d8,]
    Dia_7 = [a7,b8]
    Dia_8 = [a3,b2,c1]
    Dia_9 = [a5,b4,c3,d2,e1]
    Dia_10 = [a7,b6,c5,d4,e3,f2,g1]
    Dia_11 = [b8,c7,d6,e5,f4,g3,h2]
    Dia_12 = [d8,e7,f6,g5,h4]
    Dia_13 = [f8,g7,h6]

    Dia_14 = [b1, a2]
    Dia_15 = [d1, c2, b3, a4]
    Dia_16 = [f1, e2, d3, c4, b5, a6]
    Dia_17 = [h1, g2, f3, e4, d5, c6, b7, a8]
    Dia_18 = [c8, d7, e6, f5, g4, h3]
    Dia_19 = [e8, f7, g6, h5]
    Dia_20 = [h7, g8]
    Dia_21 = [h3, g2, f1]
    Dia_22 = [h5, g4, f3, e2, d1]
    Dia_23 = [h7, g6, f5, e4, d3, c2, b1]
    Dia_24 = [g8, f7, e6, d5, c4, b3, a2]
    Dia_25 = [e8, d7, c6, b5, a4]
    Dia_26 = [c8, b7, a6]

#Configure all squares
    Squares = [a1, b1, c1, d1, e1, f1, g1, h1,a2, b2, c2, d2, e2, f2, g2, h2,a3, b3, c3, d3, e3, f3, g3, h3,a4, b4, c4, d4, e4, f4, g4, h4,a5, b5, c5, d5, e5, f5, g5, h5,a6, b6, c6, d6, e6, f6, g6, h6,a7, b7, c7, d7, e7, f7, g7, h7,a8, b8, c8, d8, e8, f8, g8, h8]












def Squares():
    for i in range(8):
        for j in range(8):
            screen.blit(Board.board[i][j],(i * 100, j * 100))
            # if board.board.piece is not empty draw piece image
            # is board.board is selected, draw selected border
            # is board.board is colored, draw selected border diffrent color














