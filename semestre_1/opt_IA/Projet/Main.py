from Reversi import Board
from ReversiAI import ReversiAI

def print_board(board):
    print(" ", end=' ')
    for i in range(1,board.get_board_size()+1):
        print(i, end=' ')
    print()
    for i in range(1,board.get_board_size()+1):
        print(i, end=' ')
        for j in range(board.get_board_size()):
            print(board._piece2str(board._board[i-1][j]), end=' ')
        print()

def print_program_IA():
    print("""
    Depth in search algorithms signifies the number of future moves considered. A higher depth provides more accurate predictions but demands greater computation. 
    """)
    depth = int(input("Choose the depth of the AI: "))

    print("""
    Choose the method of search algorithms
    """)
    print("0: minmax lent")
    print("1: alphabeta normal")
    print("2: alphabeta opti rapide")
    x = int(input("Choose : "))
    return depth,x


def print_winner(board): 
    print_board(board)
    nb_white, nb_black = board.get_nb_pieces()
    if nb_white > nb_black:
        print("White wins!")
    elif nb_black > nb_white:
        print("Black wins!")
    else:
        print("It's a draw!")

    print("Game over!")

def humain_move(board):
    move = [board._nextPlayer, -1, -1]
    while move not in board.legal_moves():
        try:
            x = int(input("Enter row (1-{}): ".format(board._boardsize)))
            y = int(input("Enter column (1-{}): ".format(board._boardsize)))
            move = [board._nextPlayer, x-1, y-1]
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")
    return move

def main_ai_humain():
    board = Board(boardsize=10)
    depth,methode= print_program_IA()
    print("0: Humain")
    print("1: IA")
    inputCouleur = int(input("Who starts first? : "))
    couleur = None

    match inputCouleur:
        case 0:
            couleur = Board._WHITE
        case _:
            couleur = Board._BLACK

    ai = ReversiAI(player=couleur, depth=depth)

    while not board.is_game_over():
        print_board(board)
        if board._nextPlayer == ai.player:
            print("AI's turn:")
            move = ai.get_move(board,methode)
        else:
            print("Your turn:")
            move = humain_move(board)

        board.push(move)

    print_winner(board)

def main_ai_ai():
    board = Board(boardsize=10)
    depth_1,methode_1= print_program_IA()
    ai_1 = ReversiAI(player=Board._WHITE, depth=depth_1)
    depth_2,methode_2= print_program_IA()
    ai_2 = ReversiAI(player=Board._BLACK, depth=depth_2)

    while not board.is_game_over():
        print_board(board)
        print()
        if board._nextPlayer == Board._WHITE:
            move = ai_1.get_move(board,methode_1)
        else:
            move = ai_2.get_move(board,methode_2)
        board.push(move)
    print("the first IA is white: 0")
    print("the second IA is black: X")
    print_winner(board)

def main_humain_humain():
    board = Board(boardsize=10)

    while not board.is_game_over():
        print_board(board)

        if board._nextPlayer == board._BLACK:
            print("Black's Turn:")
            move = humain_move(board)
        else:
            print("White's Turn:")
            move = humain_move(board)

        board.push(move)

    print_winner(board)

if __name__ == "__main__":
    print("The player is an AI capable of playing against another AI, against a human player")
    print("0: AI against AI")
    print("1: AI against human")
    print("2: human against human")
    x = int(input("Choose game mode : "))

    match x:
        case 0:
            main_ai_ai()
        case 1:
            main_ai_humain()
        case 2:
            main_humain_humain()
        case _:
            main_ai_humain()
