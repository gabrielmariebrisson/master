from Reversi import Board
import numpy as np
import random
from random import choice

class QLearning(object): 
    def __init__(self):
        super(QLearning, self).__init__()
        self.board = Board(boardsize=10)
        if random.randint(0, 1):
            self.board._nextPlayer=Board._WHITE
        else :
            self.board._nextPlayer=Board._BLACK

    def reset(self):
        """
        Réinitialiser l'environnement
        """
        self.board = Board(boardsize=10)
        random_number = random.randint(0, 1)
        if (random_number):
            self.board._nextPlayer=Board._WHITE
        else :
            self.board._nextPlayer=Board._BLACK

    def print_Q(self, Q):  # Afficher la matrice Q
        for row in Q:
            for value in row:
                print(f"{value:.2f}\t", end="")
            print()

    def step(self, action):
        self.y = max(0, min(self.y + self.actions[action][0],2))
        self.x = max(0, min(self.x + self.actions[action][1],2))

        return (self.y*3+self.x+1) , self.grid[self.y][self.x]



    def take_action(self, Q, eps):  # Prendre une action dans l'environnement
        # Choisir une action aléatoire avec une probabilité epsilon, sinon, choisir l'action la plus avantageuse
        if random.uniform(0, 1) < eps :
            action = choice(list(self.board.legal_moves()))
        else:  # Action avantageuse
            maxvalue = float('-inf')
            for m in self.board.legal_moves():
                _, x, y = m
                if Q[x][y] > maxvalue:
                    maxvalue = Q[x][y]
                    action = m
        return action

    def q_propagation(self, state, Q, gamma, learning_rate, eps):  # Propagation de l'apprentissage par renforcement
        nbWhite=0
        nbBlack=0
        while not self.board.is_game_over():
            next_state = self.take_action( Q, eps)  # Prendre une action
            self.board.push(next_state)

            if self.board._nextPlayer== self.board._BLACK:
                reward = self.board.heuristique(player=self.board._WHITE)
            else:
                reward = self.board.heuristique(player=self.board._BLACK)

            x, y = state[1], state[2]
            x_plus, y_plus = next_state[1], next_state[2]

            # Mettre à jour la valeur Q en fonction de la récompense et de la valeur Q future
            Q[x][y] = Q[x][y] + learning_rate * (reward + gamma * Q[x_plus][y_plus] - Q[x][y])
            state = next_state
        return Q

    def normalize(self, matrix):  # Normaliser une matrice
        min_value = np.min(matrix)
        max_value = np.max(matrix)
        normalized_matrix = (2 * (matrix - min_value) / (max_value - min_value)) - 1
        normalized_matrix = normalized_matrix * 10 
        return normalized_matrix


    def getHeuristicMatrix(self, epochs=500, gamma=0.1, learning_rate=0.25, eps=0.4):  # Obtenir la matrice heuristique

        # Initialiser les valeurs Q
        Q = np.zeros((10, 10))

        for _ in range(epochs):
            # Réinitialiser le jeu
            self.reset()
            if self.board._nextPlayer==Board._BLACK:
                if random.randint(0, 1):
                    state = (_, 4, 4)
                else:
                    state = (_, 3, 3)
            else:
                if random.randint(0, 1):
                    state = (_, 4, 3)
                else:
                    state = (_, 3, 4)
            Q=self.q_propagation(state, Q, gamma, learning_rate, eps)  # Propagation de l'apprentissage

        return Q
        #return self.normalize(Q)  # Retourner la matrice normalisée Q


if __name__ == "__main__":
    ql_instance = QLearning()
    Q = ql_instance.getHeuristicMatrix()  
    ql_instance.print_Q(Q)
