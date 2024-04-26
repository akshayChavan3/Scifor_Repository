import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title("TIC TAC TOE")

        tk.Label(self.window, text="Tic Tac Toe", font=("Arial", 25)).pack()
        self.status_label = tk.Label(self.window, text="X's Turn", font=("Arial", 17), bg='green', fg="white")
        self.status_label.pack(fill=tk.X)

        self.play_again_button = tk.Button(self.window, text="Play Again", font=("Arial", 10), command=self.play_again)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.num_wins = {"X": 0, "O": 0}  # Dictionary to store number of wins for each player

        self.create_board()

    def create_board(self):
        self.play_area = tk.Frame(self.window, width=300, height=300, bg='white')
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.play_area, text=" ", width=10, height=5, command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        self.play_area.pack(padx=10, pady=10)

    def play_again(self):
        self.current_player = "X"
        for point in self.buttons:
            for button in point:
                button.configure(state=tk.NORMAL, text=" ")
        self.status_label.configure(text="X's Turn")
        self.play_again_button.pack_forget()

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.num_wins[self.current_player] += 1  # Increment win count for current player
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!\nNumber of wins for {self.current_player}: {self.num_wins[self.current_player]}")
                self.play_again_button.pack()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.play_again_button.pack()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.configure(text=f"{self.current_player}'S Turn")

    def check_winner(self):
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()
