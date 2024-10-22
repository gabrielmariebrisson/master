import logging
import pickle
from collections import defaultdict
from pprint import pprint

import numpy as np
import tqdm

logging.basicConfig(level=logging.INFO)

DISCRETIZATION_POSITION, DISCRETIZATION_VELOCITY = (
    20,
    20,
)  # number of discretized states for position and velocity
NUM_ITERATIONS = 1000  # number of iterations for value iteration
NUMBER_OF_SAMPLES = 20  # number of samples to compute transition probabilities
GAMMA = 0.99  # discount factor


def discretize_position(position, n):
    space = np.linspace(-1.2, 0.6, n)
    position = np.clip(position, -1.2, 0.6)
    for i in range(n):
        if position < space[i]:
            return i - 1
    return n - 1


def discretize_velocity(velocity, n):
    space = np.linspace(-0.07, 0.07, n)
    velocity = np.clip(velocity, -0.07, 0.07)
    for i in range(n):
        if velocity < space[i]:
            return i - 1
    return n - 1


def discretize(position, velocity, discretization):
    return discretize_position(position, discretization[0]), discretize_velocity(
        velocity, discretization[1]
    )


def sample_position_from_discretized(position, n):
    space = np.linspace(-1.2, 0.6, n)
    if position == n - 1:
        return np.random.uniform(space[position], space[position] + 0.1)
    return np.random.uniform(space[position], space[position + 1])


def sample_velocity_from_discretized(velocity, n):
    space = np.linspace(-0.07, 0.07, n)
    if velocity == n - 1:
        return np.random.uniform(space[velocity], space[velocity] + 0.01)
    return np.random.uniform(space[velocity], space[velocity + 1])


def map_state_to_continuous(state, discretization):
    return (
        sample_position_from_discretized(state[0], discretization[0]),
        sample_velocity_from_discretized(state[1], discretization[1]),
    )


def compute_new_velocity(position, velocity, action):
    new_velocity = velocity + 0.001 * (action - 1) - 0.0025 * np.cos(3 * position)
    return np.clip(new_velocity, -0.07, 0.07)


def compute_new_position(position, velocity):
    new_position = position + velocity
    return np.clip(new_position, -1.2, 0.6)


class MDP:
    def __init__(
        self,
        discretization=(DISCRETIZATION_POSITION, DISCRETIZATION_VELOCITY),
        num_samples=NUMBER_OF_SAMPLES,
        gamma=GAMMA,
    ):
        self.gamma = gamma
        self.discretization = discretization
        self.discretization_position = discretization[0]
        self.discretization_velocity = discretization[1]
        self.number_of_samples = num_samples

        self.states = {
            (i, j)
            for i in range(self.discretization_position)
            for j in range(self.discretization_velocity)
        }
        self.actions = [0, 1, 2]

        logging.info("Computing transition probabilities")
        self.transition_probabilities = self.compute_transition_probabilities()
        logging.info("Transition probabilities computed")

        logging.info("Computing rewards")
        self.rewards = self.compute_rewards()
        logging.info("Rewards computed")

    def compute_transition_probabilities(self):
        transition_probabilities = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        
        for state in self.states:
            for action in self.actions:
                # Compteur pour chaque état suivant possible
                next_state_counts = defaultdict(int)
                
                # Échantillonner NUMBER_OF_SAMPLES fois
                for _ in range(self.number_of_samples):
                    # Convertir l'état discret en état continu
                    position, velocity = map_state_to_continuous(state, self.discretization)
                    
                    # Appliquer la dynamique du système
                    new_velocity = compute_new_velocity(position, velocity, action)
                    new_position = compute_new_position(position, new_velocity)
                    
                    # Discrétiser le nouvel état
                    next_state = discretize(new_position, new_velocity, self.discretization)
                    next_state_counts[next_state] += 1
                
                # Calculer les probabilités
                for next_state, count in next_state_counts.items():
                    transition_probabilities[state][action][next_state] = count / self.number_of_samples
        
        return transition_probabilities
    
    def compute_rewards(self):
        rewards = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        
        for state in self.states:
            for action in self.actions:
                for next_state,_ in self.transition_probabilities[state][action].items():
                    # Convertir l'état suivant en position continue
                    next_position, _ = map_state_to_continuous(next_state, self.discretization)
                    
                    # Récompense de 0 si position > 0.5 (état terminal), -1 sinon
                    if next_position > 0.5:
                        rewards[state][action][next_state] = 0.0
                    else:
                        rewards[state][action][next_state] = -1.0
        
        return rewards


# Now that we have defined the MDP of the mountain car problem, we can use Value Iteration to solve it



def value_iteration(mdp, num_iterations=NUM_ITERATIONS):
    # Initialiser les valeurs à 0
    V = {state: 0.0 for state in mdp.states}
    
    for _ in range(num_iterations):
        # Faire une copie des valeurs actuelles
        V_new = V.copy()
        
        for state in mdp.states:
            # Calculer la valeur maximale sur toutes les actions
            max_value = float('-inf')
            
            for action in mdp.actions:
                # Calculer la valeur espérée pour cette action
                value = 0.0
                for next_state, prob in mdp.transition_probabilities[state][action].items():
                    reward = mdp.rewards[state][action][next_state]
                    value += prob * (reward + mdp.gamma * V[next_state])
                
                max_value = max(max_value, value)
            
            V_new[state] = max_value
        
        # Mettre à jour les valeurs
        V = V_new
    
    return V


def get_policy(mdp, V):
    policy = {}
    
    for state in mdp.states:
        # Calculer la valeur pour chaque action
        action_values = []
        
        for action in mdp.actions:
            # Calculer la valeur espérée pour cette action
            value = 0.0
            for next_state, prob in mdp.transition_probabilities[state][action].items():
                reward = mdp.rewards[state][action][next_state]
                value += prob * (reward + mdp.gamma * V[next_state])
            action_values.append(value)
        
        # Choisir l'action avec la plus grande valeur
        policy[state] = np.argmax(action_values)
    
    return policy



if __name__ == "__main__":
    logging.info("Computing MDP")
    mdp = MDP()
    logging.info("MDP computed")

    logging.info("Computing Value Iteration")
    V = value_iteration(mdp)
    logging.info("Value Iteration computed")

    logging.info("Computing policy")
    policy_mountain_car = get_policy(mdp, V)
    logging.info("Policy computed")

    # save policy to file using pickle
    with open("policy.pkl", "wb") as f:
        pickle.dump(policy_mountain_car, f)
