from random import choice
from Reversi import Board
from QLearning import QLearning
import numpy as np
#https://www.ffothello.org/informatique/algorithmes/
#https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/
class ReversiAI:
    def __init__(self, player, depth=3,Qlearning=0):
        self.player = player  # Joueur de l'IA (BLACK ou WHITE)
        self.depth = depth    # Profondeur de recherche du MiniMax
        self.Qlearning=Qlearning
        if (Qlearning==1):
            ql_instance = QLearning()
            self.HeuristicMatrix= ql_instance.getHeuristicMatrix()  
        
        if (Qlearning==2):
            self.WEIGHT_MATRIX = [
                [120, -20, 20, 5, 5, 5, 5, 20, -20, 120],
                [-20, -40, -5, -5, -5, -5, -5, -5, -40, -20],
                [20, -5, 15, 3, 3, 3, 3, 15, -5, 20],
                [5, -5, 3, 3, 3, 3, 3, 3, -5, 5],
                [5, -5, 3, 3, 3, 3, 3, 3, -5, 5],
                [5, -5, 3, 3, 3, 3, 3, 3, -5, 5],
                [5, -5, 3, 3, 3, 3, 3, 3, -5, 5],
                [20, -5, 15, 3, 3, 3, 3, 15, -5, 20],
                [-20, -40, -5, -5, -5, -5, -5, -5, -40, -20],
                [120, -20, 20, 5, 5, 5, 5, 20, -20, 120]
            ]

    def get_move(self, board, choixAlphaBeta):
        move = None  # Initialize move
        match choixAlphaBeta:
            case 1:
                print(self.depth,choixAlphaBeta )
                _, move = self.BetaAlpha(board, self.depth, float('-inf'), float('inf'))
            case _:
                print(self.depth,choixAlphaBeta )
                _, move = self.AlphaBetaOpti(board, self.depth, float('-inf'), float('inf'), True)
        return move

    def AlphaBeta(self, board, depth, alpha, beta):
        if depth == 0 or board.is_game_over():
            return board.heuristique(self.player), None
        pire = float('inf')
        best_moves = []
        legal_moves = list(board.legal_moves())  # Convertir les mouvements en liste
        for m in legal_moves:
            board.push(m)
            _, child_move = self.BetaAlpha(board, depth - 1, alpha, beta)
            val = self.evaluate_move(board,m)

            if val < pire:
                best_moves = [m]
                pire = val
            elif val == pire:
                best_moves.append(m)
            
            board.pop()
            beta = min(beta, pire)
            if alpha >= beta:
                break  # Élagage alpha-bêta
        return pire, choice(best_moves)

    def BetaAlpha(self, board, depth, alpha, beta):
        if depth == 0 or board.is_game_over():
            return board.heuristique(self.player), None
        meilleur = float('-inf')
        best_moves = []
        legal_moves = list(board.legal_moves())  # Convertir les mouvements en liste
        for m in legal_moves:
            board.push(m)
            _, child_move = self.AlphaBeta(board, depth - 1, alpha, beta)
            val = self.evaluate_move(board,m)

            if val > meilleur:
                best_moves = [m]
                meilleur = val
            elif val == meilleur:
                best_moves.append(m)
            
            board.pop()
            alpha = max(alpha, meilleur)
            if alpha >= beta:
                break  # Élagage alpha-bêta
        return meilleur, choice(best_moves)


    def AlphaBetaOpti(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return board.heuristique(self.player), None

        legal_moves = board.legal_moves()

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for move in legal_moves:
                _, child_move = self.AlphaBetaOpti(board, depth - 1, alpha, beta, False)
                evaluation = self.evaluate_move(board,move)

                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move

                alpha = max(alpha, max_eval)
                if alpha >= beta:
                    break  # Élagage alpha-bêta

            return max_eval, best_move

        else:
            min_eval = float('inf')
            best_move = None

            for move in legal_moves:
                _, child_move = self.AlphaBetaOpti(board, depth - 1, alpha, beta, True)
                evaluation = self.evaluate_move(board,move)

                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move

                beta = min(beta, min_eval)
                if alpha >= beta:
                    break  # Élagage alpha-bêta

            return min_eval, best_move



    def evaluate_move(self, board, move):
        if (self.Qlearning==0):
            return board.heuristique(self.player)
        if (self.Qlearning==2):
            return self.OpitiHeuristique(board,self.player)
        _, x,y = move
        return self.HeuristicMatrix[x][y]

    def OpitiHeuristique(self, board, player=None):
        if player is None:
            player = self._nextPlayer

        score = 0
        for x in range(10):
            for y in range(10):
                if board._board[x][y] == player:
                    score += self.WEIGHT_MATRIX[x][y]
                    neighbors = self.get_neighbors(board,x, y)
                    score += len(neighbors)
                else :
                    score -= self.WEIGHT_MATRIX[x][y]

        return score

    def get_neighbors(self,board, x, y):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < board._boardsize and 0 <= ny < board._boardsize and (dx != 0 or dy != 0):
                    neighbors.append((nx, ny))
        return neighbors



