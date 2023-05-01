import pygame

import Piece_Movement
import Piece_Placement
import board
pygame.init()

import Square_Info

screen = pygame.display.set_mode((800 , 800))

#initiating the board
from board import Board





running = True
while running:
    board.Squares()
    Piece_Placement.Default_placement()
    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # rpx/rpy stands for rounded-position-y/x
            #sq stands for square
            rpx = pos[0] - (pos[0] % 100)
            rpy = pos[1] - (pos[1] % 100)
            plx = rpx//100
            ply = rpy//100
            x_place = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
            plx = x_place.get(plx)
            y_place = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
            ply = y_place.get(ply)
            print(plx, ply)
        if event.type == pygame.QUIT:
            running = False
