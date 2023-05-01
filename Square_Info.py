import pygame
import board
class Square_Info:
    def __init__(self, color, place, IsOn, IsCons, IsPick,Bp,Wp):
        self.Bp = 'Images/blacksquare.png'
        self.Wp = 'Images/whitesquare.png'
        self.pic = pygame.image.load()
        self.trans_pic = pygame.transform.scale(self.pic, (100, 100))
        self.color = color
        self.place = place
        self.IsOn = IsOn
        self.IsCons = IsCons
        self.IsPick = IsPick
        # piece = empty




class A1_info:
    name = board.Board.a1
    Coord = "A1"
    Pixel = 0,700
    IsOn = True
    IsCons = False
    IsPicked = False
class A2_info:
    name = board.Board.a2
    Coord = "A2"
    Pixel = 0, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class A3_info:
    name = board.Board.a3
    Coord = "A3"
    Pixel = 0, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class A4_info:
    name = board.Board.a4
    Coord = "A4"
    Pixel = 0, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class A5_info:
    name = board.Board.a5
    Coord = "A5"
    Pixel = 0, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class A6_info:
    name = board.Board.a6
    Coord = "A6"
    Pixel = 0, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class A7_info:
    name = board.Board.a7
    Coord = "A7"
    Pixel = 0, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class A8_info:
    name = board.Board.a8
    Coord = "A8"
    Pixel = 0, 0
    IsOn = True
    IsCons = False
    IsPicked = False

class B1_info:
    name = board.Board.b1
    Coord = "B1"
    Pixel = 100, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class B2_info:
    name = board.Board.b2
    Coord = "B2"
    Pixel = 100, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class B3_info:
    name = board.Board.b3
    Coord = "B3"
    Pixel = 100, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class B4_info:
    name = board.Board.b4
    Coord = "B4"
    Pixel = 100, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class B5_info:
    name = board.Board.b5
    Coord = "B5"
    Pixel = 100, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class B6_info:
    name = board.Board.b6
    Coord = "B6"
    Pixel = 100, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class B7_info:
    name = board.Board.b7
    Coord = "B1"
    Pixel = 100, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class B8_info:
    name = board.Board.b8
    Coord = "B8"
    Pixel = 100, 0
    IsOn = True
    IsCons = False
    IsPicked = False
class C1_info:
    name = board.Board.c1
    Coord = "C1"
    Pixel = 200, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class C2_info:
    name = board.Board.c2
    Coord = "C2"
    Pixel = 200, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class C3_info:
    name = board.Board.c3
    Coord = "C3"
    Pixel = 200, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class C4_info:
    name = board.Board.c4
    Coord = "C4"
    Pixel = 200, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class C5_info:
    name = board.Board.c5
    Coord = "C5"
    Pixel = 200, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class C6_info:
    name = board.Board.c6
    Coord = "C6"
    Pixel = 200, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class C7_info:
    name = board.Board.c7
    Coord = "C7"
    Pixel = 200, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class C8_info:
    name = board.Board.c8
    Coord = "C8"
    Pixel = 200, 0
    IsOn = True
    IsCons = False
    IsPicked = False
class D1_info:
    name = board.Board.d1
    Coord = "D1"
    Pixel = 300, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class D2_info:
    name = board.Board.d2
    Coord = "D2"
    Pixel = 300, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class D3_info:
    name = board.Board.d3
    Coord = "D3"
    Pixel = 300, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class D4_info:
    name = board.Board.d4
    Coord = "D4"
    Pixel = 300, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class D5_info:
    name = board.Board.d5
    Coord = "D5"
    Pixel = 300, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class D6_info:
    name = board.Board.d6
    Coord = "D6"
    Pixel = 300, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class D7_info:
    name = board.Board.d7
    Coord = "D7"
    Pixel = 300, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class D8_info:
    name = board.Board.d8
    Coord = "D8"
    Pixel = 300, 0
    IsOn = True
    IsCons = False
    IsPicked = False
class E1_info:
    name = board.Board.e1
    Coord = "E1"
    Pixel = 400, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class E2_info:
    name = board.Board.e2
    Coord = "E2"
    Pixel = 400, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class E3_info:
    name = board.Board.e3
    Coord = "E3"
    Pixel = 400, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class E4_info:
    name = board.Board.e4
    Coord = "E4"
    Pixel = 400, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class E5_info:
    name = board.Board.e5
    Coord = "E5"
    Pixel = 400, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class E6_info:
    name = board.Board.e6
    Coord = "E6"
    Pixel = 400, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class E7_info:
    name = board.Board.e7
    Coord = "E7"
    Pixel = 400, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class E8_info:
    name = board.Board.e8
    Coord = "E8"
    Pixel = 400, 00
    IsOn = True
    IsCons = False
    IsPicked = False
class F1_info:
    name = board.Board.f1
    Coord = "F1"
    Pixel = 500, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class F2_info:
    name = board.Board.f2
    Coord = "F2"
    Pixel = 500, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class F3_info:
    name = board.Board.f3
    Coord = "F3"
    Pixel = 500, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class F4_info:
    name = board.Board.f4
    Coord = "F4"
    Pixel = 500, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class F5_info:
    name = board.Board.f5
    Coord = "F5"
    Pixel = 500, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class F6_info:
    name = board.Board.f6
    Coord = "F6"
    Pixel = 500, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class F7_info:
    name = board.Board.f7
    Coord = "F7"
    Pixel = 500, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class F8_info:
    name = board.Board.f8
    Coord = "F8"
    Pixel = 500, 0
    IsOn = True
    IsCons = False
    IsPicked = False
class G1_info:
    name = board.Board.g1
    Coord = "G1"
    Pixel = 600, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class G2_info:
    name = board.Board.g2
    Coord = "G2"
    Pixel = 600, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class G3_info:
    name = board.Board.g3
    Coord = "G3"
    Pixel = 600, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class G4_info:
    name = board.Board.g4
    Coord = "G4"
    Pixel = 600, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class G5_info:
    name = board.Board.g5
    Coord = "G5"
    Pixel = 600, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class G6_info:
    name = board.Board.g6
    Coord = "G6"
    Pixel = 600, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class G7_info:
    name = board.Board.g7
    Coord = "G7"
    Pixel = 600, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class G8_info:
    name = board.Board.g8
    Coord = "G8"
    Pixel = 600, 0
    IsOn = True
    IsCons = False
    IsPicked = False
class H1_info:
    name = board.Board.h1
    Coord = "H1"
    Pixel = 700, 700
    IsOn = True
    IsCons = False
    IsPicked = False
class H2_info:
    name = board.Board.h2
    Coord = "H2"
    Pixel = 700, 600
    IsOn = True
    IsCons = False
    IsPicked = False
class H3_info:
    name = board.Board.h3
    Coord = "H3"
    Pixel = 700, 500
    IsOn = False
    IsCons = False
    IsPicked = False
class H4_info:
    name = board.Board.h4
    Coord = "H4"
    Pixel = 700, 400
    IsOn = False
    IsCons = False
    IsPicked = False
class H5_info:
    name = board.Board.h5
    Coord = "H5"
    Pixel = 700, 300
    IsOn = False
    IsCons = False
    IsPicked = False
class H6_info:
    name = board.Board.h6
    Coord = "H6"
    Pixel = 700, 200
    IsOn = False
    IsCons = False
    IsPicked = False
class H7_info:
    name = board.Board.h7
    Coord = "H7"
    Pixel = 700, 100
    IsOn = True
    IsCons = False
    IsPicked = False
class H8_info:
    name = board.Board.h8
    Coord = "H8"
    Pixel = 700, 0
    IsOn = True
    IsCons = False
    IsPicked = False



