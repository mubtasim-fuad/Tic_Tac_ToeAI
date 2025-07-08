import math

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] != " " and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None

def heuristic(board, player):
    # implement later
    return 0  

def minimax(board, depth, maximizing, player):
    # NOTE: Alpha-Beta Pruning not yet implemented. Will be added later-miwan
    result = check_winner(board)
    if result is not None:
        if result == "Draw":
            return 0, None
        return (1 if result == player else -1), None

    if maximizing:
        max_eval = -math.inf
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                eval, _ = minimax(board, depth - 1, False, player)
                board[i] = " "
                if eval > max_eval:
                    max_eval = eval
                    best_move = i
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        opponent = "O" if player == "X" else "X"
        for i in range(9):
            if board[i] == " ":
                board[i] = opponent
                eval, _ = minimax(board, depth - 1, True, player)
                board[i] = " "
                if eval < min_eval:
                    min_eval = eval
                    best_move = i
        return min_eval, best_move

