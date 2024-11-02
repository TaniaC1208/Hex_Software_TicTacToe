import tkinter as tk
from tkinter import messagebox

# Initialize the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables for game state
current_player = "X"
board = [" " for _ in range(9)]
buttons = []

# Function to check for a winner and highlight winning line
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            # Highlight winning combination in blue
            for index in combo:
                buttons[index].config(bg="blue")
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
            return True

    if " " not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return True

    return False

# Function to handle player moves
def on_button_click(index):
    global current_player

    if board[index] == " ":
        # Update board and button text
        board[index] = current_player
        buttons[index].config(text=current_player)

        # Check for a winner or switch player
        if not check_winner():
            current_player = "O" if current_player == "X" else "X"
    else:
        # Notify if the clicked spot is occupied
        messagebox.showinfo("Invalid Move", "This spot is already taken!")

# Function to reset the game board
def reset_game():
    global current_player, board
    current_player = "X"
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace")

# Set up Tic-Tac-Toe buttons and board layout
for i in range(9):
    button = tk.Button(root, text=" ", font="Arial 20 bold", width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Run the main event loop
root.mainloop()
