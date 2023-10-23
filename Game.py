from Graphics import *
import pygame
from Chomp import Chomp
from Humen_Agent import Human_Agent

win = pygame.display.set_mode((WIDTH, HEIGHT))
env = Chomp()
graphics = Graphics(win, env.state)
pygame.display.set_caption('Chomp')
player1 = Human_Agent(1)
player2 = Human_Agent(2)


def main ():
    start = time.time()
    run = True
    clock = pygame.time.Clock()
    graphics.draw()
    player = player1
    
    while(run):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
        action = player.get_action(event, env, graphics)
        if action:
            env.move(action)
            player = switch_players(player)
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
    

