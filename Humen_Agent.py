import pygame
from Graphics import *
from Chomp import Chomp
from State import State

class Human_Agent:

    def __init__(self, player: int, graphics: Graphics, env: Chomp  ) -> None:
        self.player = player
        self.graphics = graphics
        self.env = env

    def get_action(self, events = None, state: State=None ,env=None ):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row_col = self.graphics.calc_row_col(pos) 
                if not self.env.is_Legal(row_col, state):
                    return None
                pygame.time.wait(500)
                return row_col
        return None