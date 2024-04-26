import tkinter as tk

class ScreenPet:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

    def draw_face(self, face):
        # Clear canvas
        self.canvas.delete("all")

        # Draw head
        self.canvas.create_oval(50, 50, 150, 150, fill="lightblue", outline="black", width=2)

        # Draw egg shape on the head
        self.canvas.create_oval(75, 25, 125, 55, fill="lightblue", outline="black", width=2)

        # Draw eyes (egg-shaped white eyes with black dots inside)
        eye_radius = 15
        eye_center1 = (90, 80)
        eye_center2 = (140, 80)
        self.canvas.create_oval(eye_center1[0] - eye_radius, eye_center1[1] - eye_radius,
                                eye_center1[0] + eye_radius, eye_center1[1] + eye_radius,
                                fill="white", outline="black", width=2)
        self.canvas.create_oval(eye_center2[0] - eye_radius, eye_center2[1] - eye_radius,
                                eye_center2[0] + eye_radius, eye_center2[1] + eye_radius,
                                fill="white", outline="black", width=2)

        # Draw black dots inside the eyes
        dot_radius = 5
        self.canvas.create_oval(eye_center1[0] - dot_radius, eye_center1[1] - dot_radius,
                                eye_center1[0] + dot_radius, eye_center1[1] + dot_radius,
                                fill="black")
        self.canvas.create_oval(eye_center2[0] - dot_radius, eye_center2[1] - dot_radius,
                                eye_center2[0] + dot_radius, eye_center2[1] + dot_radius,
                                fill="black")

        # Draw elliptical legs
        leg1 = self.canvas.create_oval(75, 150, 90, 190, fill="lightblue", outline="black", width=2)
        leg2 = self.canvas.create_oval(110, 150, 125, 190, fill="lightblue", outline="black", width=2)

        # Draw collars
        collar1 = self.canvas.create_oval(50, 55, 100, 65, fill="red", outline="black", width=2)
        collar2 = self.canvas.create_oval(110, 55, 160, 65, fill="red", outline="black", width=2)

        # Draw mouth
        if face == "happy":
            self.canvas.create_arc(80, 100, 150, 140, start=0, extent=-180, style=tk.ARC, outline="black", width=2)
        elif face == "cheeky":
            self.canvas.create_line(80, 120, 100, 110, smooth=True, width=2)
            self.canvas.create_line(150, 120, 130, 110, smooth=True, width=2)
        elif face == "sad":
            self.canvas.create_arc(80, 120, 150, 140, start=0, extent=180, style=tk.ARC, outline="black", width=2)


# Create main window
root = tk.Tk()
root.title("Screen Pet")

# Create ScreenPet instance
screen_pet = ScreenPet(root)

# Draw a happy face
screen_pet.draw_face("happy")

root.mainloop()
