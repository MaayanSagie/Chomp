from Graphics import *   
import pygame
from Chomp import Chomp
from Humen_Agent import Human_Agent
from Random_Agent import Random_Agent
from MinMaxAgent import MinMaxAgent
from AlphaBetaAgent import AlphaBeta
from DQN_Agent import DQN_Agent

win = pygame.display.set_mode((WIDTH, HEIGHT))
env = Chomp()
graphics = Graphics(win, env.state)
pygame.display.set_caption('Chomp')
# player1 = Human_Agent(1, graphics=graphics, env=env)
# player1 = MinMaxAgent(1, environment=env)
# player2 = Human_Agent(2, graphics=graphics, env=env)
# player2 = MinMaxAgent(2, environment=env)
# player1 = DQN_Agent(1, env=env, parametes_path="Data/checkpoint1.pth", train = False)
player2 = DQN_Agent(2, env=env, parametes_path="Data/checkpoint11.pth", train = False)
player1 = Random_Agent(1 , env=env)
# player2 = Random_Agent(2 , env=env)
# player1 = AlphaBeta(1, environment=env)
# player2 = AlphaBeta(2, environment=env)



def main ():
    start = time.time()
    run = True
    clock = pygame.time.Clock()
    graphics.draw()
    player = player1
    
    while(run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
        action = player.get_action(events = events, state=env.state,env=env)
        if action:
            env.move(action)
            player = switch_players(player)
            pygame.time.delay(600)
            graphics.draw()
        pygame.display.update()
        if env.is_over(env.state):
            if player == player1:
                print("player two won")
            else:
                print("player one won")
            run = False

    
def switch_players(player):
    if player == player1:
       return player2
    else:
        return player1

if __name__ == '__main__':
    main()
    

