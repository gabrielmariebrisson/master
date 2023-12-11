from random import choice
from Reversi import Board
#https://www.ffothello.org/informatique/algorithmes/
#https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/
class ReversiAI:
    def __init__(self, player, depth=3):
        self.player = player  # Joueur de l'IA (BLACK ou WHITE)
        self.depth = depth    # Profondeur de recherche du MiniMax

    def get_move(self, board, choixAlphaBeta):
        move = None  # Initialize move
        match choixAlphaBeta:
            case 0:
                print(self.depth,choixAlphaBeta )
                _, move = self.maxMin(board, self.depth, float('-inf'), float('inf') )
            case 1:
                print(self.depth,choixAlphaBeta )
                _, move = self.BetaAlpha(board, self.depth, float('-inf'), float('inf'))
            case _:
                print(self.depth,choixAlphaBeta )
                _, move = self.AlphaBetaOpti(board, self.depth, float('-inf'), float('inf'), True)
        return move



    def minMax(self, board, minimum, maximum, depth=3):
        if board.is_game_over() or depth == 0:
            return board.heuristique(self.player), None
        pire = float('inf')
        best_moves = []
        for m in board.legal_moves():
            board.push(m)
            _, child_move = self.maxMin(board, minimum, maximum, depth - 1)
            val = self.evaluate_move(board, m, child_move)

            if val < pire:
                best_moves = [m]
                pire = val
            elif val == pire:
                best_moves.append(m)
            board.pop()
            maximum = min(maximum, pire)
        return pire, choice(best_moves)  # Adjust this line to return the best move as well

    def maxMin(self, board, minimum, maximum, depth=3):
        if board.is_game_over() or depth == 0:
            return board.heuristique(self.player), None
        meilleur = float('-inf')
        best_moves = []
        for m in board.legal_moves():
            board.push(m)
            _, child_move = self.minMax(board, minimum, maximum, depth - 1)
            val = self.evaluate_move(board, m, child_move)

            if val > meilleur:
                best_moves = [m]
                meilleur = val
            elif val == meilleur:
                best_moves.append(m)

            board.pop()
            minimum = max(minimum, meilleur)
        return meilleur, choice(best_moves)  # Adjust this line to return the best move as well


    def AlphaBeta(self, board, depth, alpha, beta):
        if depth == 0 or board.is_game_over():
            return board.heuristique(self.player), None
        pire = float('inf')
        best_moves = []
        legal_moves = list(board.legal_moves())  # Convertir les mouvements en liste
        for m in legal_moves:
            board.push(m)
            _, child_move = self.BetaAlpha(board, depth - 1, alpha, beta)
            val = self.evaluate_move(board, m, child_move)

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
            val = self.evaluate_move(board, m, child_move)

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
                evaluation = self.evaluate_move(board, move, child_move)

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
                evaluation = self.evaluate_move(board, move, child_move)

                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move

                beta = min(beta, min_eval)
                if alpha >= beta:
                    break  # Élagage alpha-bêta

            return min_eval, best_move



    def evaluate_move(self, board, current_move, child_move):
        # Vous pouvez définir votre propre fonction d'évaluation ici.
        # Par exemple, comptez le nombre de pièces après le coup.
        # N'oubliez pas d'ajuster cela en fonction de votre stratégie.
        return board.heuristique(self.player)



            def minimax(self, depth, maximizing_player):
        if depth == 0 or self.is_game_over():
            return self.heuristique()

        legal_moves = self.legal_moves()

        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                child_board = copy.deepcopy(self)
                child_board.push(move)
                eval = child_board.minimax(depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                child_board = copy.deepcopy(self)
                child_board.push(move)
                eval = child_board.minimax(depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self, depth=3):
        legal_moves = self.legal_moves()
        best_move = None
        best_eval = float('-inf')

        for move in legal_moves:
            child_board = copy.deepcopy(self)
            child_board.push(move)
            eval = child_board.minimax(depth - 1, False)

            if eval > best_eval:
                best_eval = eval
                best_move = move

        return best_move
