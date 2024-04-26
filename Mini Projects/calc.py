import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry field to display and input numbers
        self.entry = tk.Entry(root, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Function to handle button clicks
        def button_click(value):
            if value == '=':
                try:
                    result = eval(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(result))
                except Exception as e:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, "Error")
            else:
                self.entry.insert(tk.END, value)

        # Create buttons and assign click function
        row, col = 1, 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

# Create the main window
root = tk.Tk()
app = CalculatorApp(root)

# Run the application
root.mainloop()
