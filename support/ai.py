import math

def check_winner(board):
    """
    Checks the board for a winner or a draw.
    Returns:
        - 'X' or 'O' if a player wins,
        - 'Draw' if the board is full with no winner,
        - None if the game is still ongoing.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] != " " and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]  # Return the winner ('X' or 'O')

    if " " not in board:
        return "Draw"

    return None  # Game still in progress

def heuristic(board, player):
    """
    Heuristic evaluation function for non-terminal game states.
    Rewards potential winning lines for the player and penalizes for the opponent's threats.
    """
    opponent = "O" if player == "X" else "X"
    score = 0

    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for line in lines:
        line_values = [board[i] for i in line]

        # Reward if the player has 2 in a line and the third is empty
        if line_values.count(player) == 2 and line_values.count(" ") == 1:
            score += 10
        # Smaller reward for one player's mark and two spaces
        elif line_values.count(player) == 1 and line_values.count(" ") == 2:
            score += 1
        # Penalize if opponent is close to winning
        if line_values.count(opponent) == 2 and line_values.count(" ") == 1:
            score -= 8

    return score

def minimax(board, depth, alpha, beta, maximizing, player, use_heuristic=False):
    """
    Minimax algorithm with alpha-beta pruning.
    Supports optional heuristic evaluation for non-terminal states when depth is 0.

    Args:
        board: Current board state (list of 9 elements).
        depth: How many moves ahead to simulate.
        alpha: Best score the maximizing player can guarantee.
        beta: Best score the minimizing player can guarantee.
        maximizing: Boolean indicating if current layer is maximizing player.
        player: The AI player's symbol ('X' or 'O').
        use_heuristic: Whether to use heuristic evaluation at depth 0.

    Returns:
        Tuple of (score, move_index).
    """
    result = check_winner(board)
    if result is not None:
        # Terminal state
        if result == "Draw":
            return 0, None
        return (1e6 if result == player else -1e6), None

    if depth == 0 and use_heuristic:
        return heuristic(board, player), None

    if maximizing:
        max_eval = -math.inf
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                eval, _ = minimax(board, depth - 1, alpha, beta, False, player, use_heuristic)
                board[i] = " "
                if eval > max_eval:
                    max_eval = eval
                    best_move = i
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        opponent = "O" if player == "X" else "X"
        for i in range(9):
            if board[i] == " ":
                board[i] = opponent
                eval, _ = minimax(board, depth - 1, alpha, beta, True, player, use_heuristic)
                board[i] = " "
                if eval < min_eval:
                    min_eval = eval
                    best_move = i
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
        return min_eval, best_move

