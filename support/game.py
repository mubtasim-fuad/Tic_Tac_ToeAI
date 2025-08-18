from .ai import minimax  # Importing the minimax function from a local ai module
import math

def print_board(board):
    """
    Prints the Tic Tac Toe board in a human-readable format.
    """
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")  # Separator between rows

def player_move(board, human_player):
    """
    Handles the player's move by taking input and validating it.
    Prompts the user until a valid move is made.
    """
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1  # Convert from 1-9 to 0-8 for list indexing
            if 0 <= move < 9 and board[move] == " ":
                board[move] = human_player  # Place the player's symbol
                break
            else:
                print("Invalid move. The cell is already occupied or out of range. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(board, ai_player, use_heuristic=False):
    """
    Determines the best move for the AI using the minimax algorithm.
    Optionally, a heuristic can be used if `use_heuristic` is True.
    """
    print("AI is thinking...")
    
    # Call minimax to determine the best move for the AI
    _, move = minimax(
        board,
        depth=9,  # Maximum depth for a full search of the game tree
        alpha=-math.inf,
        beta=math.inf,
        maximizing=True,
        player=ai_player,
        use_heuristic=use_heuristic
    )
    
    # Make the move if one was found
    if move is not None:
        board[move] = ai_player
