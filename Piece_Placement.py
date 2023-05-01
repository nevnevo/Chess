import pygame
import Square_Info
import board
pygame.init()
screen = pygame.display.set_mode((800 , 800))
class Pawns:
    #Defining white pawns
    a2_Pawn = pygame.image.load('Images/Pawn.png')
    a2_Pawn = pygame.transform.scale(a2_Pawn, (83, 83))
    b2_Pawn = pygame.image.load('Images/Pawn.png')
    b2_Pawn = pygame.transform.scale(b2_Pawn, (83, 83))
    c2_Pawn = pygame.image.load('Images/Pawn.png')
    c2_Pawn = pygame.transform.scale(c2_Pawn, (83, 83))
    d2_Pawn = pygame.image.load('Images/Pawn.png')
    d2_Pawn = pygame.transform.scale(d2_Pawn, (83, 83))
    e2_Pawn = pygame.image.load('Images/Pawn.png')
    e2_Pawn = pygame.transform.scale(e2_Pawn, (83, 83))
    f2_Pawn = pygame.image.load('Images/Pawn.png')
    f2_Pawn = pygame.transform.scale(f2_Pawn, (83, 83))
    g2_Pawn = pygame.image.load('Images/Pawn.png')
    g2_Pawn = pygame.transform.scale(g2_Pawn, (83, 83))
    h2_Pawn = pygame.image.load('Images/Pawn.png')
    h2_Pawn = pygame.transform.scale(h2_Pawn, (83, 83))



    #Defining black pawns
    a7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    a7_Pawn = pygame.transform.scale(a7_Pawn, (83, 83))
    b7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    b7_Pawn = pygame.transform.scale(b7_Pawn, (83, 83))
    c7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    c7_Pawn = pygame.transform.scale(c7_Pawn, (83, 83))
    d7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    d7_Pawn = pygame.transform.scale(c7_Pawn, (83, 83))
    e7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    e7_Pawn = pygame.transform.scale(e7_Pawn, (83, 83))
    f7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    f7_Pawn = pygame.transform.scale(f7_Pawn, (83, 83))
    g7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    g7_Pawn = pygame.transform.scale(g7_Pawn, (83, 83))
    h7_Pawn = pygame.image.load('Images/Black_Pawn.png')
    h7_Pawn = pygame.transform.scale(h7_Pawn, (83, 83))








class Pieces:
    # Defining white pieces
    a1_Rook = pygame.image.load('Images/White_Rook.png')
    a1_Rook = pygame.transform.scale(a1_Rook, (83, 83))
    h1_Rook = pygame.image.load('Images/White_Rook.png')
    h1_Rook = pygame.transform.scale(h1_Rook, (83, 83))

    b1_Knight = pygame.image.load('Images/White_Knight.png')
    b1_Knight = pygame.transform.scale(b1_Knight, (83, 83))
    g1_Knight = pygame.image.load('Images/White_Knight.png')
    g1_Knight = pygame.transform.scale(g1_Knight, (83, 83))

    c1_Bishop = pygame.image.load('Images/White_Bishop.png')
    c1_Bishop = pygame.transform.scale(c1_Bishop, (83, 83))
    f1_Bishop = pygame.image.load('Images/White_Bishop.png')
    f1_Bishop = pygame.transform.scale(f1_Bishop, (83, 83))

    e1_King = pygame.image.load('Images/White_King.png')
    e1_King = pygame.transform.scale(e1_King, (83, 83))

    d1_Queen = pygame.image.load('Images/White_Queen.png')
    d1_Queen = pygame.transform.scale(d1_Queen, (83, 83))

    #Defining black pieces
    a8_Rook = pygame.image.load('Images/Black_Rook.png')
    a8_Rook = pygame.transform.scale(a8_Rook, (83, 83))
    h8_Rook = pygame.image.load('Images/Black_Rook.png')
    h8_Rook = pygame.transform.scale(h8_Rook, (83, 83))

    b8_Knight = pygame.image.load('Images/Black_Knight.png')
    b8_Knight = pygame.transform.scale(b8_Knight, (83, 83))
    g8_Knight = pygame.image.load('Images/Black_Knight.png')
    g8_Knight = pygame.transform.scale(g8_Knight, (83, 83))

    c8_Bishop = pygame.image.load('Images/Black_Bishop.png')
    c8_Bishop = pygame.transform.scale(c8_Bishop, (83, 83))
    f8_Bishop = pygame.image.load('Images/Black_Bishop.png')
    f8_Bishop = pygame.transform.scale(f8_Bishop, (83, 83))

    e8_King = pygame.image.load('Images/Black_King.png')
    e8_King = pygame.transform.scale(e8_King, (83, 83))

    d8_Queen = pygame.image.load('Images/Black_Queen.png')
    d8_Queen = pygame.transform.scale(d8_Queen, (83, 83))








# TAL

def Default_placement():
    #Placing the  white pawns
    screen.blit(Pawns.a2_Pawn, (Square_Info.A2_info.Pixel))
    screen.blit(Pawns.b2_Pawn, (Square_Info.B2_info.Pixel))
    screen.blit(Pawns.c2_Pawn, (Square_Info.C2_info.Pixel))
    screen.blit(Pawns.d2_Pawn, (Square_Info.D2_info.Pixel))
    screen.blit(Pawns.e2_Pawn, (Square_Info.E2_info.Pixel))
    screen.blit(Pawns.f2_Pawn, (Square_Info.F2_info.Pixel))
    screen.blit(Pawns.g2_Pawn, (Square_Info.G2_info.Pixel))
    screen.blit(Pawns.h2_Pawn, (Square_Info.H2_info.Pixel))


    #Placing the black pawns
    screen.blit(Pawns.a7_Pawn, (Square_Info.A7_info.Pixel))
    screen.blit(Pawns.b7_Pawn, (Square_Info.B7_info.Pixel))
    screen.blit(Pawns.c7_Pawn, (Square_Info.C7_info.Pixel))
    screen.blit(Pawns.d7_Pawn, (Square_Info.D7_info.Pixel))
    screen.blit(Pawns.e7_Pawn, (Square_Info.E7_info.Pixel))
    screen.blit(Pawns.f7_Pawn, (Square_Info.F7_info.Pixel))
    screen.blit(Pawns.g7_Pawn, (Square_Info.G7_info.Pixel))
    screen.blit(Pawns.h7_Pawn, (Square_Info.H7_info.Pixel))



    #Placing the white pieces
    screen.blit(Pieces.a1_Rook,(Square_Info.A1_info.Pixel))
    screen.blit(Pieces.h1_Rook, (Square_Info.H1_info.Pixel))
    screen.blit(Pieces.b1_Knight, (Square_Info.B1_info.Pixel))
    screen.blit(Pieces.g1_Knight, (Square_Info.G1_info.Pixel))
    screen.blit(Pieces.c1_Bishop, (Square_Info.C1_info.Pixel))
    screen.blit(Pieces.f1_Bishop, (Square_Info.F1_info.Pixel))
    screen.blit(Pieces.e1_King, (Square_Info.E1_info.Pixel))
    screen.blit(Pieces.d1_Queen, (Square_Info.D1_info.Pixel))

    #Placing the black pieces
    screen.blit(Pieces.a8_Rook, (Square_Info.A8_info.Pixel))
    screen.blit(Pieces.h8_Rook, (Square_Info.H8_info.Pixel))
    screen.blit(Pieces.b8_Knight, (Square_Info.B8_info.Pixel))
    screen.blit(Pieces.g8_Knight, (Square_Info.G8_info.Pixel))
    screen.blit(Pieces.c8_Bishop, (Square_Info.C8_info.Pixel))
    screen.blit(Pieces.f8_Bishop, (Square_Info.F8_info.Pixel))
    screen.blit(Pieces.e8_King, (Square_Info.E8_info.Pixel))
    screen.blit(Pieces.d8_Queen, (Square_Info.D8_info.Pixel))












