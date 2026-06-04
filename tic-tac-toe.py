import math
import random

# Core Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    """Renders the game board to the console."""
    print("\n")
    for i in range(3):
        row_str = f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} "
        print(row_str)
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    """Checks if the specified player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

def board_full(board):
    """Checks if there are no empty spots left on the board."""
    return EMPTY not in board

def get_empty_cells(board):
    """Returns a list of indexes that are still available."""
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm reinforced with Alpha-Beta Pruning.
    Returns the optimal score for a given board configuration.
    """
    # Base Cases: Evaluate terminal states
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_empty_cells(board):
            board[move] = AI
            evaluation = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Beta cutoff to prune branches
        return max_eval
    else:
        min_eval = math.inf
        for move in get_empty_cells(board):
            board[move] = HUMAN
            evaluation = minimax(board, depth + 1, True, alpha, beta)
            board[move] = EMPTY
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha cutoff to prune branches
        return min_eval

def find_best_move(board):
    """Finds and returns the best move index for the AI."""
    best_score = -math.inf
    best_moves = []
    
    for move in get_empty_cells(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = EMPTY
        
        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)
            
    # Randomly choose among equally good moves to vary gameplay
    return random.choice(best_moves)

def play_game():
    """Main game loop managing turns, human input, and win states."""
    board = [EMPTY] * 9
    print("--- Welcome to Unbeatable Tic-Tac-Toe AI ---")
    print("Grid positions are numbered 1 to 9 (Top-Left to Bottom-Right):")
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")
    
    # Decide who goes first
    turn = HUMAN if input("Do you want to go first? (y/n): ").strip().lower() == 'y' else AI
    
    while True:
        print_board(board)
        
        # Check Terminal State
        if check_winner(board, HUMAN):
            print("Congratulations! You won!")
            break
        if check_winner(board, AI):
            print("AI wins! Better luck next time.")
            break
        if board_full(board):
            print("It's a draw!")
            break
            
        # Execute Current Player Move
        if turn == HUMAN:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in get_empty_cells(board):
                    board[move] = HUMAN
                    turn = AI
                else:
                    print("Invalid move! That spot is taken or out of bounds.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
        else:
            print("AI is calculating...")
            move = find_best_move(board)
            board[move] = AI
            turn = HUMAN

if __name__ == "__main__":
    play_game()
