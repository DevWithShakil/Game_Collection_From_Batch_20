def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)


def play_game():
    print("=" * 40)
    print("         TIC-TAC-TOE")
    print("=" * 40)
    print("Player 1 = X, Player 2 = O")
    print("Positions are numbered 1-9 like this:")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")

    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves_made = 0

    print_board(board)

    while True:
        move = input(f"Player {current_player}, pick a spot (1-9): ").strip()

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Please enter a number between 1 and 9.\n")
            continue

        index = int(move) - 1

        if board[index] in ("X", "O"):
            print("That spot is already taken. Try again.\n")
            continue

        board[index] = current_player
        moves_made += 1
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! Congratulations!")
            break

        if moves_made == 9:
            print("🤝 It's a tie! Good game.")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == "y":
        print()
        play_game()
    else:
        print("\nThanks for playing! 👋")


if __name__ == "__main__":
    play_game()