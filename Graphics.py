import numpy as np
import pygame
import time

ROWS, COLS = 8,8
WIDTH, HEIGHT = COLS*100, ROWS*100

SQUARE_SIZE = WIDTH//COLS
LINE_WIDTH = 2
PADDING = SQUARE_SIZE //5


#RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHTGRAY = (211,211,211)
GREEN = (0, 128, 0)

pygame.init()



class Graphics:
    def __init__(self, win, state):
        self.state = state
        self.board = self.state.board
        # rows, cols = board.shape
        self.win = win
        # self.rows = rows
        # self.cols = cols

    def draw_Lines(self):
            for i in range(ROWS):
                pygame.draw.line(self.win, BLACK, (0, i * SQUARE_SIZE), (HEIGHT, i * SQUARE_SIZE ), width=LINE_WIDTH)
                pygame.draw.line(self.win, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE , WIDTH), width=LINE_WIDTH)
                
            for i in range(COLS):
                pygame.draw.line(self.win, BLACK, (0, i * SQUARE_SIZE), (HEIGHT, i * SQUARE_SIZE ), width=LINE_WIDTH)
                pygame.draw.line(self.win, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE , WIDTH), width=LINE_WIDTH)

                
                
    def draw(self):
        self.win.fill(LIGHTGRAY)
        self.draw_Lines()
        self.draw_all_pieces()

    def draw_all_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] !=0 :
                    self.draw_piece((row, col), self.board[row][col])
            
    def draw_piece(self, row_col, player):
        center = self.calc_pos(row_col)
        radius = (SQUARE_SIZE) // 2 - PADDING
        color = self.calc_color(player)

        if player == -2:
            x,y = self.calc_base_pos(row_col)
            pygame.draw.rect(self.win,color ,pygame.Rect(x,y,SQUARE_SIZE,SQUARE_SIZE))
            
       
        pygame.draw.circle(self.win,color , center, radius)

    def calc_pos(self, row_col):
        row, col = row_col
        y = row * SQUARE_SIZE + SQUARE_SIZE//2
        x = col * SQUARE_SIZE + SQUARE_SIZE//2
        return x, y

    def calc_base_pos(self, row_col):
        row, col = row_col
        y = row * SQUARE_SIZE
        x = col * SQUARE_SIZE
        return x, y

    def calc_row_col(self, pos):
        x, y = pos
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        return row, col

    def calc_color(self, player):
        if player == 1:
            return WHITE
        elif player == 2:
            return BLACK
        elif player == -1:
            if self.state.player == 1:
                return RED
            else:
                return BLUE
        elif player == -2:
            return BLACK
        else:
            return LIGHTGRAY
    

    


 
