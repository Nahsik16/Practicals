import math

# Function to display the board
def display_board(board):
    print("Current board state:")
    for row in board:
        print("|".join(row))
    print("\n")

# Function to check if the game has ended in a win
def check_winner(board):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if ['X', 'X', 'X'] in win_conditions:
        return 'X'
    elif ['O', 'O', 'O'] in win_conditions:
        return 'O'
    else:
        return None

# Function to check if the game is over (either win or draw)
def game_over(board):
    return check_winner(board) or all(cell != ' ' for row in board for cell in row)

# Evaluation function: +1 for 'X' win, -1 for 'O' win, 0 for draw
def evaluate_position(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0

# Get available moves (empty spots on the board)
def get_children(board):
    children = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = [row[:] for row in board]  # Deep copy the board
                children.append((new_board, i, j))
    return children

# Minimax function
def minimax(board, depth, maximizingPlayer):
    if depth == 0 or game_over(board):
        return evaluate_position(board)
    if maximizingPlayer:
        maxEval = -math.inf
        for child, i, j in get_children(board):
            child[i][j] = 'X'
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for child, i, j in get_children(board):
            child[i][j] = 'O'
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval

# Function to make the best move for 'X' (AI)
def best_move(board):
    bestVal = -math.inf
    move = None
    for child, i, j in get_children(board):
        child[i][j] = 'X'
        moveVal = minimax(child, 0, False)
        if moveVal > bestVal:
            bestVal = moveVal
            move = (i, j)
    return move

# Function to let the human player make a move
def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("This cell is already occupied. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")

# Main function to play the game
def play_game():
    # Initial empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', and the computer is 'X'.")
    
    while not game_over(board):
        # Human player's move
        display_board(board)
        print("Your move (O):")
        human_move(board)

        if game_over(board):
            break

        # Computer's move
        print("Computer's move (X):")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'

    display_board(board)
    winner = check_winner(board)
    if winner == 'X':
        print("The computer wins!")
    elif winner == 'O':
        print("You win!")
    else:
        print("It's a draw!")

# Run the game
play_game()
