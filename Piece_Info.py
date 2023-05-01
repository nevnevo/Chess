import pygame
import Pieces
import board
import Square_Info
import Piece_Placement
class Piece_Info:
    #Rooks
    Piece_Placement.Pieces.a1_Rook = Pieces.Rook("White", "A1", (0, 700),  1, "A",board.Board.Dia_4, False)
    Piece_Placement.Pieces.h1_Rook = Pieces.Rook("White", "H1", (700, 700), 1, "H",board.Board.Dia_17, False)
    Piece_Placement.Pieces.a8_Rook = Pieces.Rook("Black", "A8", (0, 0), 8, "A",board.Board.Dia_4, False)
    Piece_Placement.Pieces.h8_Rook = Pieces.Rook("Black", "H8", (700, 0), 8, "H",board.Board.Dia_17, False)

    #Knights
    Piece_Placement.Pieces.b1_Knight = Pieces.Knight("White", "B1", (100, 700), 1, "B",board.Board.Dia_23,board.Board.Dia_14, True)
    Piece_Placement.Pieces.g1_Knight = Pieces.Knight("White", "G1", (600, 700), 1, "G",board.Board.Dia_10,board.Board.Dia_1, True)
    Piece_Placement.Pieces.b8_Knight = Pieces.Knight("Black", "B8", (100, 0), 8, "B",board.Board.Dia_2,board.Board.Dia_7, True)
    Piece_Placement.Pieces.g8_Knight = Pieces.Knight("Black", "G8", (600, 0), 8, "G",board.Board.Dia_24,board.Board.Dia_20, True)

    #Bishop
    Piece_Placement.Pieces.c1_Bishop = Pieces.Bishop("White", "C1", (200, 700), 1, "C",board.Board.Dia_8,board.Board.Dia_3,False)
    Piece_Placement.Pieces.f1_Bishop = Pieces.Bishop("White", "F1", (500, 700), 1, "F",board.Board.Dia_16,board.Board.Dia_21, False)
    Piece_Placement.Pieces.c8_Bishop = Pieces.Bishop("Black", "C8", (200, 0), 8, "C",board.Board.Dia_18,board.Board.Dia_26, False)
    Piece_Placement.Pieces.f8_Bishop = Pieces.Bishop("Black", "F8", (500, 0), 8, "F",board.Board.Dia_13,board.Board.Dia_5, False)

    #Queens
    Piece_Placement.Pieces.d1_Queen = Pieces.Queen("White", "D1", (300, 700), 1, "D",board.Board.Dia_15,board.Board.Dia_22, False)
    Piece_Placement.Pieces.d8_Queen = Pieces.Queen("Black", "D8", (300, 0), 8, "D",board.Board.Dia_6,board.Board.Dia_12, False)

    #Kings
    Piece_Placement.Pieces.e1_King = Pieces.King("White", "E1", (400, 700), 1, "E",board.Board.Dia_23,board.Board.Dia_14, False)
    Piece_Placement.Pieces.e8_King = Pieces.King("Black", "E8", (400, 0), 8, "E",board.Board.Dia_25,board.Board.Dia_19, False)

    #Pawns
            #White pawns
    Piece_Placement.Pieces.a2_Pawn = Pieces.Knight("White", "A2", (0, 600), 2, "A", board.Board.Dia_24,board.Board.Dia_14, True)
    Piece_Placement.Pieces.b2_Pawn = Pieces.Knight("White", "B2", (100, 600), 2, "B", board.Board.Dia_4,board.Board.Dia_8, True)
    Piece_Placement.Pieces.c2_Pawn = Pieces.Knight("White", "C2", (200, 600), 2, "C", board.Board.Dia_15,board.Board.Dia_23, True)
    Piece_Placement.Pieces.d2_Pawn = Pieces.Knight("White", "D2", (300, 600), 2, "D", board.Board.Dia_3, board.Board.Dia_9, True)
    Piece_Placement.Pieces.e2_Pawn = Pieces.Knight("White", "E2", (400, 600), 2, "E", board.Board.Dia_16,board.Board.Dia_22, True)
    Piece_Placement.Pieces.f2_Pawn = Pieces.Knight("White", "F2", (500, 600), 2, "F", board.Board.Dia_2,board.Board.Dia_10, True)
    Piece_Placement.Pieces.g2_Pawn = Pieces.Knight("White", "G2", (600, 600), 2, "G", board.Board.Dia_17, board.Board.Dia_21, True)
    Piece_Placement.Pieces.h2_Pawn = Pieces.Knight("White", "H2", (700, 600), 2, "H", board.Board.Dia_11,board.Board.Dia_1, True)

            #Black pawns
    Piece_Placement.Pieces.a7_Pawn = Pieces.Knight("Black", "A7", (0, 0), 7, "A", board.Board.Dia_7,board.Board.Dia_10, True)
    Piece_Placement.Pieces.b7_Pawn = Pieces.Knight("Black", "B7", (100, 0), 7, "B", board.Board.Dia_17,board.Board.Dia_26, True)
    Piece_Placement.Pieces.c7_Pawn = Pieces.Knight("Black", "C7", (200, 0), 7, "C", board.Board.Dia_18,board.Board.Dia_25, True)
    Piece_Placement.Pieces.d7_Pawn = Pieces.Knight("Black", "D7", (300, 0), 7, "D", board.Board.Dia_6,board.Board.Dia_11, True)
    Piece_Placement.Pieces.e7_Pawn = Pieces.Knight("Black", "E7", (400, 0), 7, "E", board.Board.Dia_5,board.Board.Dia_12, True)
    Piece_Placement.Pieces.f7_Pawn = Pieces.Knight("Black", "F7", (500, 0), 7, "F", board.Board.Dia_2,board.Board.Dia_10, True)
    Piece_Placement.Pieces.g7_Pawn = Pieces.Knight("Black", "G7", (600, 0), 7, "G", board.Board.Dia_4,board.Board.Dia_13, True)
    Piece_Placement.Pieces.h7_Pawn = Pieces.Knight("Black", "H7", (700, 0), 7, "H", board.Board.Dia_20,board.Board.Dia_23, True)




