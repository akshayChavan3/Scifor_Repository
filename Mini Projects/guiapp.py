import tkinter as tk
import random

class RandomNamePicker:
    def __init__(self, root, all_names):
        self.root = root
        self.all_names = all_names
        self.used_names = []

        # Randomly picked name label
        self.random_name_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.random_name_label.pack(pady=20)

        # Button to pick a random name
        self.pick_button = tk.Button(root, text="Pick Random Name", command=self.pick_random_name)
        self.pick_button.pack(pady=10)

        # Label for used names
        self.used_names_label = tk.Label(root, text="Names Already Picked", font=("Helvetica", 14))
        self.used_names_label.pack()

        # Text widget to display used names
        self.used_names_text = tk.Text(root, height=5, width=30)
        self.used_names_text.pack()

    def pick_random_name(self):
        if self.all_names:
            random_name = random.choice(self.all_names)
            self.all_names.remove(random_name)
            self.used_names.append(random_name)
            self.update_display()
        else:
            self.random_name_label.config(text="No more names to pick!")

    def update_display(self):
        self.random_name_label.config(text=random.choice(self.all_names))
        self.used_names_text.delete(1.0, tk.END)
        for name in self.used_names:
            self.used_names_text.insert(tk.END, name + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Random Name Picker")

    all_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]

    app = RandomNamePicker(root, all_names)

    root.mainloop()
