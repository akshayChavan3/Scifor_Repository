import tkinter as tk

class NameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gui name ")

        # Create label and entry widget
        self.label = tk.Label(master, text="Gui name:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        # Create button
        self.button = tk.Button(master, text="Submit", command=self.display_name)
        self.button.pack()

        # Create label to display name
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def display_name(self):
        name = self.entry.get()
        self.result_label.config(text=f"Your name is: {name}")

root = tk.Tk()
app = NameApp(root)
root.mainloop()
