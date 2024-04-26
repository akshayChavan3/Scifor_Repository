import tkinter as tk

def create_labels():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Label Example")

    # Create labels with different text
    label1 = tk.Label(window, text="Label 1")
    label2 = tk.Label(window, text="Label 2")
    label3 = tk.Label(window, text="Label 3")

    # Pack the labels to the window
    label1.pack()
    label2.pack()
    label3.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Call the function to create labels
create_labels()
