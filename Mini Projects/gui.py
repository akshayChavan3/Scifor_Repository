import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        # Create canvas
        self.canvas = tk.Canvas(master, width=400, height=400, bg="green")
        self.canvas.pack()

        # Draw squares
        self.draw_square(50, 50, 150, 150)
        self.draw_square(200, 50, 300, 150)
        self.draw_square(50, 200, 150, 300)
        self.draw_square(200, 200, 300, 300)

    def draw_square(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="red")

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
