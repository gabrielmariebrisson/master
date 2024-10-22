import numpy as np

class Env:
    def __init__(self, n_states, n_actions):
        self.n_states = n_states
        self.n_actions = n_actions
        self.transitions = np.random.rand(n_states, n_actions, n_states)
        self.rewards = np.random.rand(n_states, n_actions)
        self.initial_state = 0

    def reset(self):
        return self.initial_state
    
    def play(self, state, action):
        next_state = np.random.choice(self.n_states, p=self.transitions[state, action])
        reward = self.rewards[state, action]
        return next_state, reward


class Env1(Env):
    def __init__(self):
        super().__init__(n_states=2, n_actions=2)
        self.transitions = np.array([[[0.5, 0.5], [1./3, 2./3]], [[0, 1.], [0, 1.]]])
        self.rewards = np.array([[2, 4], [10, 10]])

    def is_terminal(self, state):
        return state == 1

class Env2(Env):
    def __init__(self):
        super().__init__(n_states=3, n_actions=3)
        self.transitions = np.array([[[1., 0., 0], [0., 1., 0.], [0., 0., 1.]], 
                                     [[1., 0., 0], [0., 1., 0.], [0., 0., 1.]],
                                     [[0., 1., 0], [1., 0., 0.], [0., 0., 1.]]])
        self.rewards = np.array([[1, 1.5, 1.], [0.5, 1, 1.5], [1., 1., 1.]])

    def is_terminal(self, state):
        return state == 2

class Env3(Env):
    def __init__(self):
        super().__init__(n_states=3, n_actions=2)
        self.transitions = np.array([[[1., 0.], [0., 1.], [0., 0.]], 
                                [[1., 0.], [0., 1.], [0., 0.]],
                                [[0.,  0], [1., 0.], [0., 0.]]])
        self.rewards = np.array([[1, 2], [1, 2], [2, 2]])

    def is_terminal(self, state):
        return state == 2

if __name__ == '__main__':
    env = Env1()
    print(env.reset())
    print(env.play(0, 0))
    print(env.play(1, 1))