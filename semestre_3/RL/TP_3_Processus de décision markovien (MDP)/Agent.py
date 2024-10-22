class Agent:
    def __init__(self, num_states, num_actions, policy):
        """
        Initializes an Agent with the given parameters.
        :param num_states: Number of states in the environment.
        :param num_actions: Number of actions available.
        :param policy: A policy function or table that maps states to actions.
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.policy = policy  # Can be a function or a lookup table
    
    # Getter and Setter methods for the attributes
    def get_num_states(self):
        return self.num_states
    
    def set_num_states(self, num_states):
        self.num_states = num_states
    
    def get_num_actions(self):
        return self.num_actions
    
    def set_num_actions(self, num_actions):
        self.num_actions = num_actions
    
    def get_policy(self):
        return self.policy
    
    def set_policy(self, policy):
        self.policy = policy

    def choose_action(self, state):
        """
        Returns the action based on the current policy for state s.
        :param state: The current state.
        :return: The action selected by the policy for the given state.
        """
        if callable(self.policy):  # If the policy is a function
            return self.policy(state)
        elif isinstance(self.policy, dict):  # If the policy is a lookup table (dict)
            return self.policy.get(state, None)
        else:
            raise ValueError("Policy must be a function or a dictionary mapping states to actions.")
