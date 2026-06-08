"""
CodSoft AI Internship - Task 2
Tic-Tac-Toe AI using Minimax Algorithm
Author: Goush Shaik
"""

import math
import random

HUMAN = "X"
AI = "O"
EMPTY = " "


def make_board():
    return [EMPTY] * 9


def print_board(board):
    print()

    for row in range(3):
        cells = board[row * 3: row * 3 + 3]
        print(f" {cells[0]} | {cells[1]} | {cells[2]}")

        if row < 2:
            print("---+---+---")

    print()


def print_position_guide():
    print("\nPosition Guide:")

    for row in range(3):
        nums = [str(row * 3 + col + 1) for col in range(3)]

        print(f" {nums[0]} | {nums[1]} | {nums[2]}")

        if row < 2:
            print("---+---+---")

    print()


WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),

    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    (0, 4, 8),
    (2, 4, 6)
]


def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def is_board_full(board):
    return EMPTY not in board


def check_winner(board, player):

    for a, b, c in WIN_COMBINATIONS:

        if board[a] == board[b] == board[c] == player:
            return True

    return False


def game_over(board):

    return (
        check_winner(board, HUMAN)
        or check_winner(board, AI)
        or is_board_full(board)
    )


def minimax(board, depth, is_maximizing):

    if check_winner(board, AI):
        return 10 - depth

    if check_winner(board, HUMAN):
        return depth - 10

    if is_board_full(board):
        return 0

    if is_maximizing:

        best_score = -math.inf

        for cell in get_empty_cells(board):

            board[cell] = AI

            score = minimax(board, depth + 1, False)

            board[cell] = EMPTY

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for cell in get_empty_cells(board):

            board[cell] = HUMAN

            score = minimax(board, depth + 1, True)

            board[cell] = EMPTY

            best_score = min(best_score, score)

        return best_score


def get_best_move(board):

    best_score = -math.inf
    best_move = None

    for cell in get_empty_cells(board):

        board[cell] = AI

        score = minimax(board, 0, False)

        board[cell] = EMPTY

        if score > best_score:
            best_score = score
            best_move = cell

    return best_move


def get_human_move(board):

    while True:

        try:

            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")

            elif board[move] != EMPTY:
                print("That position is already occupied.")

            else:
                return move

        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():

    board = make_board()

    print("\n" + "=" * 45)
    print("      Tic-Tac-Toe AI")
    print("      CodSoft Internship Task 2")
    print("=" * 45)

    print_position_guide()

    human_turn = random.choice([True, False])

    if human_turn:
        print("You go first.\n")
    else:
        print("AI goes first.\n")

    while not game_over(board):

        print_board(board)

        if human_turn:

            move = get_human_move(board)

            board[move] = HUMAN

        else:

            print("AI is making a move...")

            move = get_best_move(board)

            board[move] = AI

            print(f"AI selected position {move + 1}")

        human_turn = not human_turn

    print_board(board)

    if check_winner(board, HUMAN):
        print("Congratulations! You win!")

    elif check_winner(board, AI):
        print("AI wins!")

    else:
        print("The game is a draw.")


def main():

    while True:

        play_game()

        choice = input("\nPlay again? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for playing.")
            break


if __name__ == "__main__":
    main()