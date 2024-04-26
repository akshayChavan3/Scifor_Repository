import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+pen_size, y+pen_size, fill=color.get(), outline='')

def change_pen_size(size):
    global pen_size
    pen_size = size

def clear_canvas():
    canvas.delete("all")

window = tk.Tk()
window.title("Simple Paint")

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Define pen size
pen_size = 5

# Create buttons
color = tk.StringVar()
color.set("black")

btn_pen = tk.Button(window, text="Pen", command=lambda: change_pen_size(5))
btn_pen.pack(side=tk.LEFT)

btn_brush = tk.Button(window, text="Brush", command=lambda: change_pen_size(10))
btn_brush.pack(side=tk.LEFT)

btn_color = tk.Button(window, text="Color", command=lambda: color.set(tk.colorchooser.askcolor()[1]))
btn_color.pack(side=tk.LEFT)

btn_eraser = tk.Button(window, text="Eraser", command=lambda: color.set("white"))
btn_eraser.pack(side=tk.LEFT)

btn_clear = tk.Button(window, text="Clear", command=clear_canvas)
btn_clear.pack(side=tk.LEFT)

# Bind mouse events
canvas.bind("<B1-Motion>", draw)

window.mainloop()
