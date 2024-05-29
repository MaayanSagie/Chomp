from Random_Agent import Random_Agent
# from Fix_Agent import Fix_Agent
from Chomp import Chomp
from Constant import *
from DQN_Agent import DQN_Agent

class Tester:
    def __init__(self, env, player1, player2) -> None:
        self.env = env
        self.player1 = player1
        self.player2 = player2
        

    def test (self, games_num):
        env = self.env
        player = self.player1
        player1_win = 0
        player2_win = 0
        games = 0
        while games < games_num:
            action = player.get_action(state=env.state, train = False)
            env.move(action)
            player = self.switchPlayers(player)
            if env.is_over(env.state):
                # score = env.state.score()
                reward = env.reward(state=env.state)
                if reward[0] > 0:
                    player1_win += 1
                elif reward[0] < 0:
                    player2_win += 1
                env.state = env.get_init_state((ROWS,COLS))
                games += 1
                player = self.player1
        return player1_win, player2_win        

    def switchPlayers(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def __call__(self, games_num):
        return self.test(games_num)

if __name__ == '__main__':
    env = Chomp()
    # player1 = DQN_Agent(env=env, player=1, parametes_path="Data/params_2.pth", train=False)
    player1 = Random_Agent(env=env, player=1)
    player2 = Random_Agent(env=env, player=2)
    test = Tester(env,player1, player2)
    print(test.test(100))
    