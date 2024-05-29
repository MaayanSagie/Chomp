import pygame
from Graphics import *
from Chomp import Chomp
from State import State
import random


class Random_Agent:

    def __init__(self, player: int, env: Chomp  ) -> None:
        self.player = player
        self.env = env

    def get_action(self, events=None, state: State=None ,env=None ,train = None):
        legal_actions = self.env.get_legal_actions(state)
        action = random.choice(legal_actions)
        return action
    