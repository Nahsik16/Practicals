import math

# Check if the game has ended in a win
def check_winner(board):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Rows
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],  # Columns
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],  # Diagonals
        [board[0][2], board[1][1], board[2][0]]
    ]
    if ['X', 'X', 'X'] in win_conditions:
        return 'X'
    elif ['O', 'O', 'O'] in win_conditions:
        return 'O'
    return None

# Check if the game is over (either win or draw)
def game_over(board):
    return check_winner(board) or all(cell != ' ' for row in board for cell in row)

# Evaluate position: +1 for 'X' win, -1 for 'O' win, 0 for draw
def evaluate_position(board):
    winner = check_winner(board)
    return 1 if winner == 'X' else -1 if winner == 'O' else 0

# Get available moves (empty spots on the board)
def get_children(board, player):
    return [([row[:] for row in board], i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Minimax function
def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate_position(board)
    
    best_eval = -math.inf if maximizing_player else math.inf
    for child, i, j in get_children(board, 'X' if maximizing_player else 'O'):
        child[i][j] = 'X' if maximizing_player else 'O'  # Set the new move
        eval = minimax(child, depth - 1, not maximizing_player)
        best_eval = max(best_eval, eval) if maximizing_player else min(best_eval, eval)
    return best_eval

# Function to make the best move for 'X'
def best_move(board):
    best_val = -math.inf
    move = None
    for child, i, j in get_children(board, 'X'):
        child[i][j] = 'X'  # Set the new move
        move_val = minimax(child, 0, False)
        if move_val > best_val:
            best_val = move_val
            move = (i, j)
    return move

# Example Tic-Tac-Toe board state
board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    [' ', ' ', 'O']
]

# Finding the best move for 'X'
print("Best move for 'X':", best_move(board))
