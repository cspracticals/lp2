import random

# Function to display the Tic-Tac-Toe board with a creative UI
def print_board(board):
    print("\n")
    print(f" {board[0]} │ {board[1]} │ {board[2]} ")
    print("───┼───┼───")
    print(f" {board[3]} │ {board[4]} │ {board[5]} ")
    print("───┼───┼───")
    print(f" {board[6]} │ {board[7]} │ {board[8]} ")
    print("\n")

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return " " not in board

# Function for the AI to make a move (random)
def ai_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty_spots)

# Function to play the game
def play_game(mode):
    board = [" " for _ in range(9)]  # Initialize empty board
    current_player = "X"

    while True:
        print_board(board)

        # Check for win or tie
        if check_win(board, "X"):
            print("Player X wins! 🎉")
            break
        if check_win(board, "O"):
            if mode == "1":
                print("Computer wins! 🤖")
            else:
                print("Player O wins! 🎉")
            break
        if check_tie(board):
            print("It's a tie! 🙂‍↕️")
            break

        # Player X's turn
        if current_player == "X":
            try:
                move = int(input("Player X, enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move! Try again.")
                    continue
                board[move] = "X"
                current_player = "O"
            except ValueError:
                print("Please enter a valid number (1-9).")

        # Player O's turn
        elif current_player == "O":
            if mode == "1":  # Computer's turn
                move = ai_move(board)
                print(f"Computer chooses position {move + 1}")
                board[move] = "O"
                current_player = "X"
            else:  # Player O's turn
                try:
                    move = int(input("Player O, enter your move (1-9): ")) - 1
                    if move < 0 or move > 8 or board[move] != " ":
                        print("Invalid move! Try again.")
                        continue
                    board[move] = "O"
                    current_player = "X"
                except ValueError:
                    print("Please enter a valid number (1-9).")

# Main menu
def main():
    print("Welcome to Tic-Tac-Toe! 🎮")
    while True:
        print("\nSelect game mode:")
        print("1. Player vs. Computer")
        print("2. Player vs. Player")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            play_game("1")
        elif choice == "2":
            play_game("2")
        elif choice == "3":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the game
if __name__ == "__main__":
    main()