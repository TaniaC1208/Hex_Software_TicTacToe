import random

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Display the game board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check for a win
def check_win(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check for a draw
def check_draw():
    return " " not in board

# Player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("This spot is already taken!")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Computer's move
def computer_move():
    possible_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(possible_moves)
    board[move] = "O"

# Main game loop
def play_game():
    display_board()
    while True:
        player_move()
        display_board()
        if check_win("X"):
            print("Congratulations! You won!")
            break
        if check_draw():
            print("It's a draw!")
            break

        computer_move()
        display_board()
        if check_win("O"):
            print("Computer wins! Better luck next time.")
            break
        if check_draw():
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()
