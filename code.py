import math

def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} ")
    print("-----------")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("-----------")
    print(f" {b[6]} | {b[7]} | {b[8]} \n")

def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]            # Diagonals
    ]
    for condition in win_conditions:
        if b[condition[0]] == b[condition[1]] == b[condition[2]] == player:
            return True
    return False

def is_board_full(b):
    return ' ' not in b

def get_empty_cells(b):
    return [i for i, cell in enumerate(b) if cell == ' ']

# Minimax Algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):  # AI wins
        return 1
    if check_winner(b, 'X'):  # Human wins
        return -1
    if is_board_full(b):      # Tie
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for cell in get_empty_cells(b):
            b[cell] = 'O'
            eval = minimax(b, depth + 1, False)
            b[cell] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for cell in get_empty_cells(b):
            b[cell] = 'X'
            eval = minimax(b, depth + 1, True)
            b[cell] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

# Find the best move for the AI
def best_move(b):
    best_score = -math.inf
    move = -1
    for cell in get_empty_cells(b):
        b[cell] = 'O'
        score = minimax(b, 0, False)
        b[cell] = ' '
        if score > best_score:
            best_score = score
            move = cell
    return move

# Interactive Game Loop
def play_game():
    board = [' ' for _ in range(9)]
    print("Tic-Tac-Toe: You are 'X', AI is 'O'")
    print("Positions are numbered 1 to 9 like this:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \n")

    current_player = 'X'  # Human goes first

    while True:
        print_board(board)
        
        if current_player == 'X':
            # Take input safely from user (1-9)
            try:
                move = int(input("Enter your move (1-9): "))
                # Adjust for 0-indexed internal board (1-9 becomes 0-8)
                index = move - 1
                if move < 1 or move > 9 or board[index] != ' ':
                    print("Invalid move! Choose an empty spot between 1 and 9.")
                    continue
            except ValueError:
                print("Please enter a valid integer between 1 and 9.")
                continue
            
            board[index] = 'X'
            
            if check_winner(board, 'X'):
                print_board(board)
                print("Congratulations! You win!")
                break
            current_player = 'O'
        else:
            print("AI is thinking...")
            move = best_move(board)
            board[move] = 'O'
            
            if check_winner(board, 'O'):
                print_board(board)
                print("AI wins! Better luck next time.")
                break
            current_player = 'X'

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
