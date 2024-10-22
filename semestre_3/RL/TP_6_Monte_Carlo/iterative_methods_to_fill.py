import pprint as pp

from grid_world import GridWorldMDP

GAMMA = 0.9

gridworld = GridWorldMDP(10, 10, 30)


def policy_evaluation(gridworld: GridWorldMDP, policy, num_iterations=100):
    value_policy = {state: 0 for state in gridworld.states}
    for _ in range (num_iterations):
        for s in gridworld.states:
            a = policy[s]
            value_policy[s] = sum(
                    [
                    gridworld.transition_probabilities[(s,a,new_s)]*
                    gridworld.rewards[(s, a, new_s)]
                    +GAMMA*value_policy[new_s]
                    ]
                for new_s in gridworld.states
                )
                
    # TODO: Implement the function
    return value_policy


def value_iteration(gridworld: GridWorldMDP, num_iterations=100) -> dict:
    """Compute the optimal value function for the given gridworld"""
    optimal_values = {state: 0 for state in gridworld.states}
    # TODO: Implement the function
    for _ in range (num_iterations):
        for s in gridworld.states:
            a = policy[s]
            optimal_values[s] = max(sum(
                    [
                    gridworld.transition_probabilities[(s,a,new_s)]*
                    gridworld.rewards[(s, a, new_s)]
                    +GAMMA*optimal_values[new_s]
                    ]
                for new_s in gridworld.states
                ))
                
    return optimal_values


def get_policy_from_value_function(
    gridworld: GridWorldMDP, value_function: dict
) -> dict:
    """Compute the optimal policy given the value function"""
    policy = {state: (1, 0) for state in gridworld.states}
    # TODO: Implement the function
    return policy


optimal_values = value_iteration(gridworld, num_iterations=100)
gridworld.print_value_function(optimal_values)
optimal_policy = get_policy_from_value_function(gridworld, optimal_values)
gridworld.print_policy(optimal_policy)
