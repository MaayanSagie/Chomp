import pygame
from Graphics import *
from Chomp import Chomp
from State import State
MAXSCORE = 1000

class AlphaBeta:
    def __init__(self, player, depth = 2, environment: Chomp = None):
        self.player = player
        if self.player == 1:
            self.opponent = 2
        else:
            self.opponent = 1
        self.depth = depth
        self.environment : Chomp = environment
    
    def nothing():
        # def huristic_score_func(self, state, action):
        #     next_state = Chomp.next_state(state, action) 
        #     rows , cols = ROWS , COLS
        #     row = 0
        #     black_count = -1
        #     for col in cols:
        #         if next_state[row,col] == -1:
        #                 colom_count = 0
        #                 for row in rows:
        #                     if next_state[row,col] == -1:
        #                         colom_count+=1
        #                     else:
        #                         break
        #         if black_count == -1: 
        #             black_count == colom_count
        #         else:
        #             if black_count != colom_count:
        #                 return -1
        #         black_count = colom_count
        #     return 1
        pass

    def evaluate(self, state: State):
        rows , cols = ROWS , COLS
        count_row_white = 0
        count_col_white = 0
        
        count_row_white = np.count_nonzero(state.board[7,:]==0)
        count_col_white = np.count_nonzero(state.board[:,0]==0)
        score = 0

        # for row in range(rows): 
        #     if state.board[row,0] == 1:
        #         count_row_white += 1
        # for col in range(cols):
        #     if state.board[rows -1,col] == 1:
        #         count_col_white += 1
        if count_col_white == count_row_white and state.board[6,1] == -2:
            score = 1
        elif count_col_white == count_row_white and state.board[6,1] != -2:
            score = -1
        elif count_col_white != count_row_white and state.board[6,1] == -2:
            score= -1
        elif count_col_white != count_row_white and state.board[6,1] != -2:
            score = 0
        
        if state.player == self.player:
            return -score
        else:
            return score
            

    def get_action(self, events=None, state: State = None,env=None, train=None):
        value, bestAction = self.minMax(state)
        return bestAction

    def minMax(self, state:State):
        visited = set()
        depth = 0
        alpha = -MAXSCORE
        beta = MAXSCORE
        return self.max_value(state, visited, depth, alpha, beta)
        
    def max_value (self, state:State, visited:set, depth, alpha, beta):
        
        value = -MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_over(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            if action == (6, 1):
                x=1
            newState = self.environment.get_next_state(action=action, state=state)
            if newState not in visited:
                # visited.add(newState)
                newValue, newAction = self.min_value(newState, visited,  depth + 1, alpha, beta)
                if newValue > value:
                    value = newValue
                    if value == 1000:
                        x=1
                    bestAction = action
                    alpha = max(alpha, value)
                if value >= beta:
                    return value, bestAction
                

        return value, bestAction 

    def min_value (self, state:State, visited:set, depth, alpha, beta):
        
        value = MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_over(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action=action, state=state)
            if newState not in visited:
                # visited.add(newState)
                newValue, newAction = self.max_value(newState, visited,  depth + 1 , alpha, beta)
                if newValue < value:
                    value = newValue
                    bestAction = action
                    beta = min(beta, value)
                if value <= alpha:
                    return value, bestAction

        return value, bestAction 


        
                  





