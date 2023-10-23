import numpy as np

class State:
    def __init__(self, board= None, player = 1) -> None:
        self.board = board
        self.player = player
        
    def __eq__(self, other) ->bool:
        b1 = np.equal(self.board, other.board).all()
        b2 = self.player == other.player
        return np.equal(self.board, other.board).all() and self.player == other.player

    def __hash__(self) -> int:
        return hash(repr(self.board) + repr(self.player))
    
    def copy (self):
        newBoard = np.copy(self.board)
        return State(board=newBoard, player=self.player)
    
