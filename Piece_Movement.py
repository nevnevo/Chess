import pygame
import board
import Square_Info
import Piece_Placement
class Piece:

    def _init_(self, color, name):
        self.name = name
        self.position = None
        self.Color = color

    def isValid(self, startpos, endpos, Color, gameboard):
        if endpos in self.availableMoves(startpos[0], startpos[1], gameboard, Color=Color):
            return True
        return False

    def _repr_(self):
        return self.name

    def _str_(self):
        return self.name

    def availableMoves(self, x, y, gameboard):
        print("ERROR: you cant move like that")


def kingList(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]




WHITE = "white"
BLACK = "black"


class King(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return [(xx,yy) for xx,yy in kingList(x,y) if self.noConflict(gameboard, Color, xx, yy)]

def isCheck(self):
    kingDict = {}
    pieceDict = {BLACK: [], WHITE: []}
    for position, piece in self.gameboard.items():
        if type(piece) == King:
            kingDict[piece.Color] = position
        print(piece)
        pieceDict[piece.Color].append((piece, position))
    # white
    if self.canSeeKing(kingDict[WHITE], pieceDict[BLACK]):
        self.message = "White player is in check"
    if self.canSeeKing(kingDict[BLACK], pieceDict[WHITE]):
        self.message = "Black player is in check"


def canSeeKing(self, kingpos, piecelist):
    for piece, position in piecelist:
        if piece.isValid(position, kingpos, piece.Color, self.gameboard):
            return True


