import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Import Image and ImageTk from PIL

def create_window(image_file):
    # Create a new window
    window = tk.Toplevel(root)

    # Display the image using a label
    label = tk.Label(window, image=image_file)
    label.pack()

# Create the main window
root = tk.Tk()
root.title("Multiple Image Windows")

from PIL import Image, ImageTk

from PIL import Image, ImageTk

# List of image files
image_files = [r"C:\Users\sures\PycharmProjects\ endangered animals\tiger-2535888_640.jpg",
               r"C:\Users\sures\PycharmProjects\endangered animals\lion.jpg",
               r"C:\Users\sures\PycharmProjects\ endangered animals\1698912318-8f8354e46b0a88ca473607040e6b6304f59b627fcf0131685a8a5cfc43db4278-d_640x360.jpg",
               r"C:\Users\sures\PycharmProjects\ endangered animals\360_F_402953557_SWyol1myqjPhM5UcZOGPwifZWWTOYQlq.jpg"]

# Create PhotoImage objects for each image
images = []
for file in image_files:
    try:
        img = Image.open(file)
        images.append(ImageTk.PhotoImage(img))
    except Exception as e:
        print(f"Error loading image from {file}: {e}")

# Print statements to check if images are loaded
print("Number of images:", len(images))

# Create a window for each image
for image in images:
    create_window(image)

# Start the Tkinter event loop
root.mainloop()
