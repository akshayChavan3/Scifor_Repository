import tkinter as tk

# Create a set of elements in a series of 20
element_series = set(f"Element {i+1}" for i in range(20))

def display_elements():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Element Set")

    # Create a listbox and insert the elements
    listbox = tk.Listbox(window)
    for element in element_series:
        listbox.insert(tk.END, element)

    # Pack the listbox to the window
    listbox.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Call the function to display the elements
display_elements()
