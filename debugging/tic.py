#!/usr/bin/env python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves_made = 0  # Track total moves to detect a tie

    while True:
        print_board(board)

        # Get valid row input
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue
        if row not in [0, 1, 2]:
            print("Invalid row. Please enter 0, 1, or 2.")
            continue

        # Get valid column input
        try:
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue
        if col not in [0, 1, 2]:
            print("Invalid column. Please enter 0, 1, or 2.")
            continue

        # Check if the spot is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player
        moves_made += 1

        # Check for a winner immediately after the move
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # If no winner yet and 9 moves are made, it's a tie
        if moves_made == 9:
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()

