import numpy as np
from Grid import Grid

# A function that samples a random action from the set of possible actions.
def random_action(grid):
    return np.random.choice(grid.get_possible_actions())
    
# Write a function random trajectory that takes a grid and a number of steps as input 
# and returns a list of states and a list of rewards.
def random_trajectory(grid, n_steps):
    player_state = grid._get_state()
    state, reward, final, actions = grid.move(Grid.ACTION_NOP)
    while not final and n_steps>0:
        action = random_action(grid)
        print(grid.move(action) )
        grid.print()
        state, reward, final, actions = grid.move(Grid.ACTION_NOP)
        n_steps-=1 

def Q(grid, Qgrid,depth, action=Grid.ACTION_NOP, gamma=0.5):
    state, reward, final, actions = grid.move(action)
    state_position = grid._id_to_position(state)

    if final:
        Qgrid[state_position[0], state_position[1]] = reward
        return reward, Qgrid
    if Qgrid[state_position[0], state_position[1]]!= None:
        return 0, Qgrid
    
    q_values = []
    for nextAction in actions:
        future_reward, _ = Q(grid, Qgrid,depth+1, nextAction, gamma)
        q_values.append(future_reward)
    print(state_position[0], state_position[1])

    Qgrid[state_position[0], state_position[1]] = reward + gamma**depth * np.max(q_values)
    return reward, Qgrid


# main program:
# Create a grid and discover its properties and methods.
size=[3,3]
grid = Grid(size[0],size[1])
print("_________init_________")
grid.print()
print("_______position_______")
print(grid._id_to_position(grid._get_state()))
#random_trajectory(grid, 100)
Qgrid = np.full((size[0],size[1]), None, dtype=object)

print("_______debut_______")
Qgrid = Q(grid, Qgrid,0, action = Grid.ACTION_NOP)
print("_______fin_______")
print(Qgrid)

