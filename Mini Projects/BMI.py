import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class BMIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Tracker")

        self.height_unit = tk.StringVar()
        self.weight_unit = tk.StringVar()
        self.height = tk.DoubleVar()
        self.weight = tk.DoubleVar()
        self.bmi = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Height:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.master, text="Weight:").grid(row=1, column=0, padx=5, pady=5)

        self.height_scale = tk.Scale(self.master, from_=0, to=250, orient=tk.HORIZONTAL, variable=self.height)
        self.height_scale.grid(row=0, column=1, padx=5, pady=5)

        self.weight_scale = tk.Scale(self.master, from_=0, to=250, orient=tk.HORIZONTAL, variable=self.weight)
        self.weight_scale.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.master, text="Height Unit:").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.master, text="Weight Unit:").grid(row=1, column=2, padx=5, pady=5)

        height_unit_options = ["cm", "inches"]
        self.height_unit.set(height_unit_options[0])  # Default unit
        weight_unit_options = ["kg", "lbs"]
        self.weight_unit.set(weight_unit_options[0])  # Default unit

        self.height_unit_menu = tk.OptionMenu(self.master, self.height_unit, *height_unit_options)
        self.height_unit_menu.grid(row=0, column=3, padx=5, pady=5)

        self.weight_unit_menu = tk.OptionMenu(self.master, self.weight_unit, *weight_unit_options)
        self.weight_unit_menu.grid(row=1, column=3, padx=5, pady=5)

        self.calculate_button = tk.Button(self.master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=1, padx=5, pady=5)

        self.bmi_scale = tk.Scale(self.master, from_=0, to=40, orient=tk.HORIZONTAL, variable=self.bmi)
        self.bmi_scale.grid(row=3, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self.master, text="Save BMI Report", command=self.save_report)
        self.save_button.grid(row=4, column=1, padx=5, pady=5)

    def calculate_bmi(self):
        height = self.height.get()
        weight = self.weight.get()

        if self.height_unit.get() == "inches":
            height *= 2.54  # Convert inches to cm

        if self.weight_unit.get() == "lbs":
            weight *= 0.453592  # Convert lbs to kg

        if height == 0:
            messagebox.showerror("Error", "Height cannot be zero.")
            return

        bmi = weight / ((height / 100) ** 2)
        self.bmi.set(bmi)

        if bmi < 18.5:
            self.bmi_scale.configure(bg="red")
        elif bmi >= 18.5 and bmi <= 24.9:
            self.bmi_scale.configure(bg="green")
        elif bmi > 24.9:
            self.bmi_scale.configure(bg="red")

    def save_report(self):
        height_unit = self.height_unit.get()
        weight_unit = self.weight_unit.get()
        height = self.height.get()
        weight = self.weight.get()
        bmi = self.bmi.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = f"Date: {date}\nHeight: {height} {height_unit}\nWeight: {weight} {weight_unit}\nBMI: {bmi}\n\n"

        with open("bmi_reports.txt", "a") as file:
            file.write(report)

        messagebox.showinfo("Success", "BMI Report saved successfully.")


def main():
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
