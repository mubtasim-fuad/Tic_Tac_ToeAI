from support.game import print_board, ai_move, player_move
from support.ai import check_winner

def main():
    board = [" "] * 9
    human_player = ""
    ai_player = ""

    while human_player not in ["X", "O"]:
        human_player = input("Choose your side (X/O): ").upper()

    ai_player = "O" if human_player == "X" else "X"
    current_player = "X"

    print("\nBoard positions:")
    print(" 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9\n")
    print("Game start!\n")

    use_heuristic = False  # Heuristics

    while True:
        print_board(board)
        result = check_winner(board)
        if result is not None:
            print("It's a draw!" if result == "Draw" else f"{result} wins!")
            break

        if current_player == human_player:
            player_move(board, human_player)
        else:
            ai_move(board, ai_player, use_heuristic)

        current_player = "O" if current_player == "X" else "X"
        print()

if __name__ == "__main__":
    main()
