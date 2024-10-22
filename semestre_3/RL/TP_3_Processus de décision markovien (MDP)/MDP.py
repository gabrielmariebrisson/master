class MDP:
    def __init__(self, num_states, num_actions, gamma=0.9, start_state=0):
        """
        Initializes an MDP with given parameters.
        :param num_states: Number of states in the environment.
        :param num_actions: Number of actions in the environment.
        :param gamma: Discount factor for future rewards.
        :param start_state: The initial state.
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.gamma = gamma
        self.current_state = start_state
        self.start_state = start_state
        self.transition_function = {}  # e.g., {(state, action): next_state}
        self.reward_function = {}  # e.g., {(state, action): reward}
    
    # Getter and Setter methods for the attributes
    def get_num_states(self):
        return self.num_states
    
    def set_num_states(self, num_states):
        self.num_states = num_states
    
    def get_num_actions(self):
        return self.num_actions
    
    def set_num_actions(self, num_actions):
        self.num_actions = num_actions
    
    def get_gamma(self):
        return self.gamma
    
    def set_gamma(self, gamma):
        self.gamma = gamma
    
    def get_current_state(self):
        return self.current_state
    
    def set_current_state(self, state):
        self.current_state = state
    
    def get_start_state(self):
        return self.start_state
    
    def set_start_state(self, start_state):
        self.start_state = start_state

    def set_transition(self, state, action, next_state):
        """
        Sets the transition for a given (state, action) pair.
        """
        self.transition_function[(state, action)] = next_state
    
    def set_reward(self, state, action, reward):
        """
        Sets the reward for a given (state, action) pair.
        """
        self.reward_function[(state, action)] = reward
    
    def play(self, action):
        """
        Receives an action and returns the next state and the reward.
        :param action: Action to take from the current state.
        :return: (next_state, reward)
        """
        if (self.current_state, action) in self.transition_function:
            next_state = self.transition_function[(self.current_state, action)]
            reward = self.reward_function.get((self.current_state, action), 0)
            self.current_state = next_state
            return next_state, reward
        else:
            raise ValueError("Invalid action or state-action pair.")

    def get_possible_actions(self, state):
        """
        Receives a state and returns the list of possible actions.
        :param state: Current state.
        :return: List of possible actions.
        """
        return [action for (s, action) in self.transition_function.keys() if s == state]

    def simulate(self, agent, steps, detailed=False):
        """
        Simulates the agent's interaction with the MDP for a given number of steps.
        :param agent: Agent interacting with the MDP.
        :param steps: Number of steps to simulate.
        :param detailed: Whether to return detailed history or just the total reward.
        :return: Either the total reward (if detailed=False) or a list of (state, action, reward) tuples (if detailed=True).
        """
        total_reward = 0
        history = []
        
        for _ in range(steps):
            action = agent.choose_action(self.current_state)
            next_state, reward = self.play(action)
            total_reward += reward
            if detailed:
                history.append((self.current_state, action, reward))
        
        if detailed:
            return history
        else:
            return total_reward
