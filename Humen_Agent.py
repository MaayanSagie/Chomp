import pygame
from Graphics import *
from Chomp import Chomp

class Human_Agent:

    def __init__(self, player: int) -> None:
        self.player = player

    def get_action(self, event, env: Chomp, graphics: Graphics  ):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row_col = graphics.calc_row_col(pos) 
            pygame.time.wait(500)
            return row_col
        else:
            return None