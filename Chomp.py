import numpy as np
from State import State
from Graphics import *

class Chomp:
    def __init__(self, state:State = None) -> None:
        if state == None:
            self.state = self.get_init_state((ROWS, COLS))
        else:
            self.state = state

    def get_init_state(self, Rows_Cols):
        rows, cols = Rows_Cols
        board = np.zeros([rows, cols],int)
        board[ROWS-1][0] = -1
   
        return State (board, 1)

    def move(self, action):
        if not self.is_Legal(action, self.state):
            return
        row,col = action
        for i in range(row+1):
            for j in range(col, COLS):
                self.state.board[i][j] = -2
        if self.state.player == 1:
            self.state.player =2
        else:
            self.state.player =1

    def is_Legal(self, action, state):
        row, col = action
        if self.state.board[row][col] == 0:
            return True
        return False

    def is_over(self,state):
        if state.board[ROWS -2][0] == -2 and state.board[ROWS-1][1] == -2:
            return True
        return False