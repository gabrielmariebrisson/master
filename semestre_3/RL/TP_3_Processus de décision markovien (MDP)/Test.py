import random
import MDP
import Agent

# Example random policy function
def random_policy(state):
    return random.choice([0, 1, 2])  # Assuming 3 actions

# Create an agent with a random policy
agent = Agent(num_states=5, num_actions=3, policy=random_policy)

# Choose an action for a specific state
action = agent.choose_action(2)
print(action)  # Random action from [0, 1, 2]
