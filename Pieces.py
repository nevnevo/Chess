import pygame
import board
import Square_Info
import Piece_Placement
import Piece_Movement





class Rook:
    def __init__(self,color,place,pixel , row,file,dia_1,dia_2,canmove):
        self.Color = color
        self.Dia1 = dia_1
        self.Dia2 = dia_2
        self.Pixel = pixel
        self.Place = place
        self.Row = row
        self.File = file
        self.Canmove = canmove
class Knight:
    def __init__(self,color,place,pixel,row,file,dia_1,dia_2,canmove):
        self.Dia1 = dia_1
        self.Dia2 = dia_2
        self.Color = color
        self.Pixel = pixel
        self.Place = place
        self.Row = row
        self.File = file
        self.Canmove = canmove
class Bishop:
    def __init__(self,color,place,pixel,row,file,dia_1,dia_2,canmove):
        self.Dia1 = dia_1
        self.Dia2 = dia_2
        self.Color = color
        self.Pixel = pixel
        self.Place = place
        self.Row = row
        self.File = file
        self.Canmove = canmove
class Queens:
    def __init__(self,color,place,pixel,row,file,dia_1,dia_2,canmove):
        self.Dia1 = dia_1
        self.Dia2 = dia_2
        self.Color = color
        self.Pixel = pixel
        self.Place = place
        self.Row = row
        self.File = file
        self.Canmove = canmove
class Kings:
    def __init__(self,color,place,pixel,row,file,dia_1,dia_2,canmove):
        self.Dia1 = dia_1
        self.Dia2 = dia_2
        self.Color = color
        self.Pixel = pixel
        self.Place = place
        self.Row = row
        self.File = file
        self.Canmove = canmove
class Pawns:
    def __init__(self,color,place,pixel,row,file,dia_1,dia_2,canmove,moved):
        self.Dia1 = dia_1
        self.Dia2 = dia_2
        self.Color = color
        self.Pixel = pixel
        self.Place = place
        self.Row = row
        self.File = file
        self.Canmove = canmove












