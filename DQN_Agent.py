import torch
import random
import math
from DQN import DQN
from Constant import *
from State import State
from Chomp import Chomp
class DQN_Agent:
    def __init__(self, player = 1, parametes_path = None, train = True, env= None):
        self.DQN = DQN()
        if parametes_path:
            self.DQN.load_params(parametes_path)
        self.player = player
        self.train = train
        self.setTrainMode()

    def setTrainMode (self):
          if self.train:
              self.DQN.train()
          else:
              self.DQN.eval()

    def get_action (self, state:State, epoch = 0, events= None, train = True, graphics = None, env:Chomp = None) -> tuple:
        actions = state.legal_actions()
        if self.train and train:
            epsilon = self.epsilon_greedy(epoch)
            rnd = random.random()
            if rnd < epsilon:
                return random.choice(actions)
        
        state_tensor = state.toTensor()
        action_tensor = torch.tensor(actions)
        
        expand_state_tensor = state_tensor.unsqueeze(0).repeat((len(action_tensor),1))
        
        with torch.no_grad():
            Q_values = self.DQN(expand_state_tensor, action_tensor)
        max_index = torch.argmax(Q_values)
        return actions[max_index]

    def get_actions (self, states_tensor, dones) -> torch.tensor:
        actions = []

        for i, board in enumerate(states_tensor):
            if dones[i].item():
                actions.append((0,0))
            else:
                actions.append(self.get_action(State.tensorToState(state_tensor=states_tensor[i],player=self.player), train=False))
        return torch.tensor(actions)

    def epsilon_greedy(self,epoch, start = epsilon_start, final=epsilon_final,decay=epsiln_decay): # start = 1; finnish = 0.01 ; decay = 2500
        if epoch > decay:
            return final
        return start - (start - final) * epoch/decay
        
    
    def loadModel (self, file):
        self.model = torch.load(file)
    
    def save_param (self, path):
        self.DQN.save_params(path)

    def load_params (self, path):
        self.DQN.load_params(path)

    def __call__(self, events= None, state=None):
        return self.get_action(state)
