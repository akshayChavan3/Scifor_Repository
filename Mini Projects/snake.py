import tkinter as tk
import random

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake Game")
        self.canvas = tk.Canvas(self, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.create_food()
        self.direction = "Left"
        self.bind("<Key>", self.change_direction)
        self.game_loop()

    def create_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="red")
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key in ["Left", "Right", "Up", "Down"]:
            self.direction = key

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == "Left":
            x -= 10
        elif self.direction == "Right":
            x += 10
        elif self.direction == "Up":
            y -= 10
        elif self.direction == "Down":
            y += 10
        self.snake.insert(0, (x, y))
        if (x, y) == self.food:
            self.food = self.create_food()
        else:
            self.canvas.delete(self.snake.pop())
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")

    def game_loop(self):
        self.move_snake()
        self.after(100, self.game_loop)

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
