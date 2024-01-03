import numpy as np
import math

def create_board():
    return np.zeros((6, 7), dtype=int)

def print_board(board):
    for row in board:
        print("|", end=" ")
        for cell in row:
            if cell == 0:
                print(" ", end=" ")
            elif cell == 1:
                print("X", end=" ")
            elif cell == 2:
                print("O", end=" ")
        print("|")
    print("+-" * 7 + "+")
    print("  1 2 3 4 5 6 7")

def is_valid_move(board, col):
    return board[0][col] == 0

def drop_piece(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            break

def is_winner(board, player):
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertically
    for row in range(3):
        for col in range(7):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonally (from bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    return False

def evaluate_window(window, player):
    score = 0

    opp_player = 3 - player

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_player) == 3 and window.count(0) == 1:
        score -= 4

    return score

def evaluate_board(board, player):
    score = 0

    # Evaluate center column
    center_array = [int(i) for i in list(board[:, 3])]
    center_count = center_array.count(player)
    score += center_count * 3

    # Evaluate Horizontal
    for row in range(6):
        row_array = [int(i) for i in list(board[row, :])]
        for col in range(4):
            window = row_array[col:col + 4]
            score += evaluate_window(window, player)

    # Evaluate Vertical
    for col in range(7):
        col_array = [int(i) for i in list(board[:, col])]
        for row in range(3):
            window = col_array[row:row + 4]
            score += evaluate_window(window, player)

    # Evaluate Diagonal /
    for row in range(3, 6):
        for col in range(4):
            window = [board[row - i][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    # Evaluate Diagonal \
    for row in range(3):
        for col in range(4):
            window = [board[row + i][col + i] for i in range(4)]
            score += evaluate_window(window, player)

    return score

def is_board_full(board):
    return all(board[0][i] != 0 for i in range(7))

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_board_full(board) or is_winner(board, 1) or is_winner(board, 2):
        return evaluate_board(board, 2) - evaluate_board(board, 1)

    valid_moves = [col for col in range(7) if is_valid_move(board, col)]

    if maximizing_player:
        max_eval = -math.inf
        for col in valid_moves:
            temp_board = np.copy(board)
            drop_piece(temp_board, col, 2)
            eval = minimax(temp_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for col in valid_moves:
            temp_board = np.copy(board)
            drop_piece(temp_board, col, 1)
            eval = minimax(temp_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_score = -math.inf
    best_move = -1

    valid_moves = [col for col in range(7) if is_valid_move(board, col)]

    for col in valid_moves:
        temp_board = np.copy(board)
        drop_piece(temp_board, col, 2)
        score = minimax(temp_board, 3, -math.inf, math.inf, False)

        if score > best_score:
            best_score = score
            best_move = col

    return best_move

def play_connect_four():
    board = create_board()
    current_player = 1

    while True:
        print_board(board)

        if current_player == 1:
            print("Player X's turn")
            col = int(input("Enter your move (column 1-7): ")) - 1
            if not is_valid_move(board, col):
                print("Invalid move. Try again.")
                continue
        else:
            print("AI's turn (Player O)")
            col = find_best_move(board)

        drop_piece(board, col, current_player)

        if is_winner(board, current_player):
            print_board(board)
            if current_player == 1:
                print("Player X wins!")
            else:
                print("Player O (AI) wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 3 - current_player  # Switch player

if __name__ == "__main__":
    play_connect_four()
