import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.resizable(False, False)
window.title("TIC TAC TOE")

tk.Label(window, text="Tic Tac Toe", font=("Ariel", 25)).pack()
status_Label = tk.Label(window, text="X's Turn", font=("Ariel", 17), bg='green', fg="white")
status_Label.pack(fill=tk.X)


def play_again():
    global current_chr
    current_chr = "X"
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_Label.configure(text="X's Turn")
    play_again_button.pack_forget()


play_again_button = tk.Button(window, text="Play Again", font=("Ariel", 10), command=play_again)

current_chr = "X"
XO_points = []
X_points = []
O_points = []
play_area = tk.Frame(window, width=300, height=300, bg='white')


class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text=" ", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg="snow", fg="black")
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
                status_Label.configure(text="O'S Turn")
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
                status_Label.configure(text="X'S Turn")

    def reset(self):
        self.button.configure(text=" ", bg='lightgray')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None


for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))

play_area.pack(padx=10, pady=10)
window.mainloop()

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.num_wins = {"X": 0, "O": 0}  # Dictionary to store number of wins for each player

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=('Arial', 30), width=5, height=2,
                                                command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.num_wins[self.current_player] += 1  # Increment win count for current player
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!\n"
                                              f"Number of wins for {self.current_player}: {self.num_wins[self.current_player]}")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

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

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def run(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.create_board()
        self.window.mainloop()

game = TicTacToe()
game.run()

gui = TicTacToeGUI()
gui.run()
