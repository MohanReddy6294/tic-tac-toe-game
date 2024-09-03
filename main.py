import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")

def move(board):
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(available_moves)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human player starts

    while True:
        print_board(board)
        if current_player == "X":
            print("Your turn!")
            row, col = get_move(board)
        else:
            print("Computer's turn!")
            row, col = move(board)

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
