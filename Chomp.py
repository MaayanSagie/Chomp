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

    # @staticmethod
    def next_state(self, state : State, action):
        row,col = action
        for i in range(row+1):
            for j in range(col, COLS):
                state.board[i][j] = -2
        if state.player == 1:
            state.player =2
        else:
            state.player =1
        return state
    
    def get_next_state (self, state, action):
        next_state = state.copy()
        next_state = self.next_state(next_state, action)
        return next_state

    def move(self, action):
        # if not self.is_Legal(action, self.state):
        #     return
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

    def get_legal_actions (self, state: State):
        indices = np.where(state.board==0)
        legal_actions = list(zip(indices[0], indices[1])) 
        return legal_actions

    def is_over(self,state):
        if state.board[ROWS -2][0] == -2 and state.board[ROWS-1][1] == -2:
            return True
        return False
    
    def reward (self, state : State, action = None) -> tuple:
        if action:
            next_state = self.get_next_state(action, state)
        else:
            next_state = state
        if self.is_over(next_state):
            if next_state.player == 1:
                return -1, True  
            elif  next_state.player == 2:
                return 1, True  
            else:
                return 0, True  
        return 0, False
    