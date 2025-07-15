from support.game import print_board, ai_move, player_move
from support.ai import check_winner

def main():
    # Initialize an empty Tic Tac Toe board
    board = [" "] * 9
    human_player = ""
    ai_player = ""

    # Ask the player to choose a side
    while human_player not in ["X", "O"]:
        human_player = input("Choose your side (X/O): ").upper()

    ai_player = "O" if human_player == "X" else "X"
    current_player = "X"  # X always starts first

    # Show the numbered board layout
    print("\nBoard positions:")
    print(" 1 | 2 | 3")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 7 | 8 | 9\n")
    print("Game start!\n")

    
    # Ask if AI should use a heuristic at limited depth
    use_heuristic = input("Limit search depth using a heuristic evaluation? (y/n): ").lower() == "y"

    # Main game loop
    while True:
        print_board(board)
        
        # Check for winner or draw after each move
        result = check_winner(board)
        if result is not None:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        # Determine whose turn it is
        if current_player == human_player:
            player_move(board, human_player)
        else:
            ai_move(board, ai_player, use_heuristic)

        # Swap turn
        current_player = "O" if current_player == "X" else "X"
        print()  # Newline for better readability

if __name__ == "__main__":
    main()
  
