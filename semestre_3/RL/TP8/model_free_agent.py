import numpy as np
from envs import Env1

class MonteCarloAgent:
    def __init__(self, env, gamma=0.9, epsilon=0.1):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.V = np.zeros(self.env.n_states)
        self.N = np.zeros(self.env.n_states)
        self.Q = np.zeros((self.env.n_states, self.env.n_actions))
        self.Nsa = np.zeros( (self.env.n_states, self.env.n_actions) )
        self.policy = np.random.randint(0, self.env.n_actions, self.env.n_states)
    
    def generate_trajectory(self):
        trajectory = []
        state = self.env.reset()
        while not self.env.is_terminal(state):
            if np.random.rand() < self.epsilon:
                action = np.random.choice(self.env.n_actions)
            else:
                action = self.policy[state] 
            new_state, reward = self.env.play(state, action)
            trajectory.append((state, action, reward))
            state = new_state
            #print(new_state)
        return trajectory

    def update(self, trajectory):
        G =0 
        for (state, action , reward) in reversed(trajectory):
            G = reward + self.gamma * G
            self.N[state] +=1
            self.Nsa[state, action] +=1
            self.V[state] += (G - self.V[state])/self.N[state]
            self.Q[state, action] += (G - self.Q[state, action])/self.Nsa[state, action]

            self.policy[state] = np.argmax(self.Q[state])


    def train(self, n_trajectories):
        # for _ in range(n_trajectories):
        #     G = 0
        #     trajectory = self.generate_trajectory()
        #     for (state, action, reward) in reversed(trajectory):
        #         G= reward+self.gamma *G
        #         self.N[state] += 1
        #         self.V[state] += (G - self.V[state])/self.N[state]
        for _ in range (n_trajectories):
            trajectory = self.generate_trajectory()
            self.update(trajectory)

class SARSAAgent:
    def __init__(self, env, gamma=0.9, epsilon=0.1, alpha = 0.1):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.alpha = alpha
        self.Q = np.zeros((self.env.n_states, self.env.n_actions))

    def generate_trajectory(self):
        trajectory = []
        state = self.env.reset()
        while not self.env.is_terminal(state):
            if np.random.rand() < self.epsilon:
                action = np.random.choice(self.env.n_actions)
            else:
                action = np.argmax(self.Q[state])
            new_state, reward = self.env.play(state, action)

            if np.random.rand() < self.epsilon:
                next_action = np.random.choice(self.env.n_actions)
            else:
                next_action = np.argmax(self.Q[new_state])
            trajectory.append((state, action, reward, new_state, next_action))
            state = new_state
            #print(new_state)
        return trajectory

    def update(self, trajectory):
        for (state, action , reward, new_state, next_action) in reversed(trajectory):
            G = reward + self.gamma * self.Q[new_state, next_action] - self.Q[state, action]
            self.Q[state, action] = self.Q[state, action] + self.alpha * G

    def train(self, n_trajectories):
        for _ in range (n_trajectories):
            trajectory = self.generate_trajectory()
            self.update(trajectory)


class QLearningAgent:
    def __init__(self, env, gamma=0.9, epsilon=0.1, alpha = 0.1):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.alpha = alpha
        self.Q = np.zeros((self.env.n_states, self.env.n_actions))

    def generate_trajectory(self):
        trajectory = []
        state = self.env.reset()
        while not self.env.is_terminal(state):
            if np.random.rand() < self.epsilon:
                action = np.random.choice(self.env.n_actions)
            else:
                action = np.argmax(self.Q[state])
            new_state, reward = self.env.play(state, action)

            next_action = np.argmax(self.Q[new_state]) #Changement de SARSA

            trajectory.append((state, action, reward, new_state, next_action))
            state = new_state
            #print(new_state)
        return trajectory

    def update(self, trajectory):
        for (state, action , reward, new_state, next_action) in reversed(trajectory):
            G = reward + self.gamma * self.Q[new_state, next_action] - self.Q[state, action]
            self.Q[state, action] = self.Q[state, action] + self.alpha * G

    def train(self, n_trajectories):
        for _ in range (n_trajectories):
            trajectory = self.generate_trajectory()
            self.update(trajectory)

class DoubleQLearningAgent:
    def __init__(self, env, gamma=0.9, epsilon=0.1, alpha = 0.1):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.alpha = alpha
        self.Q1 = np.zeros((self.env.n_states, self.env.n_actions))
        self.Q2 = np.zeros((self.env.n_states, self.env.n_actions))

    def generate_trajectory(self):
        trajectory = []
        state = self.env.reset()
        while not self.env.is_terminal(state):
            if np.random.rand() < self.epsilon:
                action = np.random.choice(self.env.n_actions)
            else:
                action = np.argmax(self.Q1[state])
            new_state, reward = self.env.play(state, action)

            next_action = np.argmax(self.Q1[new_state]) #Changement de SARSA

            trajectory.append((state, action, reward, new_state, next_action))
            state = new_state
            #print(new_state)
        return trajectory

    def update(self, trajectory):
        for (state, action , reward, new_state, next_action) in reversed(trajectory):
            G = reward + self.gamma * self.Q2[new_state, self.Q1[new_state, next_action]] - self.Q1[state, action]
            self.Q1[state, action] = self.Q1[state, action] + self.alpha * G

    def train(self, n_trajectories):
        for _ in range (n_trajectories):
            trajectory = self.generate_trajectory()
            self.update(trajectory)



if __name__=='__main__':
    env = Env1()
    # trajectory = agent.generate_trajectory()
    # print(trajectory)

    # #######____MonteCarloAgent___######
    # agent = MonteCarloAgent(env)
    # agent.train(1000)
    # print("V :", agent.V)

    #######____SARSAAgent___######
    agent = SARSAAgent(env)
    print("Old Policy \n", np.argmax(agent.Q, axis=1))
    agent.train(1000)
    print("Q :", agent.Q)

    # #######____QLearningAgent___######
    # agent = QLearningAgent(env)
    # print("Old Policy \n", np.argmax(agent.Q, axis=1))
    # agent.train(1000)
    # print("Q :", agent.Q)
    