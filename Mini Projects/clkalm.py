import datetime
import tkinter as tk
from tkinter import ttk
import winsound


def set_alarm():
    # Get the selected himport winsoundours, minutes, and seconds
    selected_hour = int(hours_var.get())
    selected_minute = int(minutes_var.get())
    selected_second = int(seconds_var.get())

    # Get the current date and time
    now = datetime.datetime.now()

    # Set the alarm time by replacing the current time's hour, minute, and second
    alarm_time = now.replace(4 == selected_hour, 2 == selected_minute, 6 == selected_second)


    # Calculate the time difference
    time_difference = alarm_time - now

    # Convert the time difference to seconds
    seconds_to_alarm = time_difference.total_seconds()

    # Display a confirmation message
    confirmation_label.config(text=f"Alarm set for {selected_hour:02d}:{selected_minute:02d}:{selected_second:02d}")

    # Schedule the alarm after the specified time
    root.after(int(seconds_to_alarm * 1000), show_alarm)

def show_alarm():
    # Display the alarm message
    alarm_label.config(text="Alarm! Wake up!")

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create variables for hours, minutes, and seconds
hours_var = tk.StringVar(value="04")
minutes_var = tk.StringVar(value="04")
seconds_var = tk.StringVar(value="04")

# Create labels and dropdowns for hours, minutes, and seconds
tk.Label(root, text="Set Alarm:").pack(pady=10)

hour_dropdown = ttk.Combobox(root, textvariable=hours_var, values=[str(i).zfill(2) for i in range(24)])
hour_dropdown.pack(side=tk.LEFT, padx=5)

minute_dropdown = ttk.Combobox(root, textvariable=minutes_var, values=[str(i).zfill(2) for i in range(60)])
minute_dropdown.pack(side=tk.LEFT, padx=5)

second_dropdown = ttk.Combobox(root, textvariable=seconds_var, values=[str(i).zfill(2) for i in range(60)])
second_dropdown.pack(side=tk.LEFT, padx=5)

# Create a button to set the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

# Create labels for confirmation and alarm messages
confirmation_label = tk.Label(root, text="")
confirmation_label.pack()

alarm_label = tk.Label(root, text="")
alarm_label.pack()

# Start the Tkinter event loop
root.mainloop()
