import numpy as np
from Reversi import Board

class QLearningReversi:
    def __init__(self, board_size=10, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.board_size = board_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = np.zeros((board_size, board_size, 3))  # 3 for each possible action: [0, 1, 2] (pass, x, y)
        self.board = Board(board_size)

    def select_action(self, state):
        if np.random.rand() < self.exploration_rate:
            # Explore: choose a random action
            return self.explore()
        else:
            # Exploit: choose the action with the highest Q-value
            x, y = self.exploit(state)
            return x, y

    def explore(self):
        legal_moves = self.board.legal_moves()
        return legal_moves[np.random.choice(len(legal_moves))]

    def exploit(self, state):
        # Convert the state to numeric coordinates (assuming state is a string representation)
        x, y = self.state_to_coordinates(state)
        return x, y

    def state_to_coordinates(self, state):
        # Extract coordinates from the string representation of the state
        # Implement this method based on the format of your state string
        # For example, if your state string is "XOXXXXX", you can do:
        lines = state.split("\n")
        pieces_line = lines[0]
        x, y = None, None
        for i, piece in enumerate(pieces_line):
            if piece == 'X' or piece == 'O':
                # Assuming 'X' represents BLACK and 'O' represents WHITE
                x, y = i // self.board_size, i % self.board_size
                break
        return x, y

    def update_q_table(self, state, action, reward, next_state):
        x, y = action[1], action[2]
        next_x, next_y = next_state[1], next_state[2]

        current_q_value = self.q_table[x, y, action[0]]
        max_next_q_value = np.max(self.q_table[next_x, next_y])

        new_q_value = (1 - self.learning_rate) * current_q_value + \
                      self.learning_rate * (reward + self.discount_factor * max_next_q_value)

        self.q_table[x, y, action[0]] = new_q_value

    def train(self, episodes=1000):
        for episode in range(episodes):
            self.board.reset()
            state = self.board.__str__()

            while not self.board.is_game_over():
                x, y = self.select_action(state)
                action = [state, x, y]
                toflip = self.board.testAndBuild_ValidMove(action[0], action[1], action[2])

                if isinstance(toflip, list):
                    self.board.push(action)
                    next_state = self.board.__str__()
                    reward = self.board.heuristique()
                    self.update_q_table(state, action, reward, next_state)
                    state = next_state

            # Print some information about the training progress
            if episode % 100 == 0:
                print(f"Episode {episode}/{episodes}")

if __name__ == "__main__":
    ql_instance = QLearningReversi()
    Q = ql_instance.train()
