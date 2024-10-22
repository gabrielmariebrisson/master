import grid_world
import random
import numpy as np

GAMMA =  0.9

class MonteCarloAgent:
    def __init__(self,env, policy=None):
        self.env = env
        if policy !=None:
            self.policy = policy
        else :
            self.policy = {state: np.random.choice(len(self.env.actions)) for state in self.env.states}
        self.V = {state: 0 for state in self.env.states}
        self.Q = {state: {action: 0 for action in self.env.actions} for state in self.env.states}

    def generate_episode(self):
        episode=[]
        s = self.env.initial_state
        terminate = self.env.terminal_state 
        while (s != terminate):
            a = self.policy[s]
            new_s, r = self.env.play(s, a)
            episode.append(s,a,r)
            s= new_s
        return episode
    
    def update_V(self,episode):
        G=0
        counter_s = [0]*len(self.env.states)
        for s,_,r in reversed(episode):
            G = r + GAMMA * G 
            counter_s[s]+=1
            self.V[s] += self.V[s] + 1/counter_s[s] *(G - self.V[s])
            

    def update_Q(self,episode):
        G=0
        counter_s_a = [0]*len(self.env.states)*len(self.env.actions)
        for s,a,r in reversed(episode):
            G = r + GAMMA * G 
            counter_s_a[(s,a)]+=1
            self.Q[s][a] += self.Q[s][a] + 1/counter_s_a[(s,a)] *(G - self.Q[s][a])

    def train(self, n_episodes =1000):
        for i in range(n_episodes):
            episode = self.generate_episode()
            self.update_V(episode)
            self.update_Q(episode)
        self.env.print_value_function(self.V)
