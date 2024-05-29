import numpy as np
import torch

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

    def score (self):
        pass

    def legal_actions(self):
        indices = np.where(self.board==0)
        legal_actions = list(zip(indices[0], indices[1])) 
        return legal_actions
    
    def toTensor (self, device = torch.device('cpu')) -> tuple:
        board_np = self.board.reshape(-1)
        board_tensor = torch.tensor(board_np, dtype=torch.float32, device=device)
        # actions_np = np.array(self.legal_actions)
        # actions_tensor = torch.from_numpy(actions_np)
        return board_tensor #, actions_tensor
    
    [staticmethod]
    def tensorToState (state_tensor, player):
        board_tensor = state_tensor
        board = board_tensor.reshape((8,8),board_tensor).cpu().numpy()
        return State(board, player=player)