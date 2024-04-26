from tkinter import *
import datetime
import time
import threading
import winsound

# Function to start a new thread for the alarm
def Threading():
    t1 = threading.Thread(target=alarm)
    t1.start()

# Function to check and play the alarm
def alarm():
    # Infinite Loop
    while True:
        # Set alarm time
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Check whether set alarm is equal to the current time
        if current_time == set_alarm_time:
            # Playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

# Create the main window
root = Tk()
root.title("Alarm Clock")

# Add Labels
label = Label(root, text="Set Your Alarm", font=("Helvetica 20 bold"), fg="red")
label.pack(pady=20)

# Add Frames
frame = Frame(root)
frame.pack()

# Add Optionmenus for hours, minutes, and seconds
hours = StringVar(root)
minutes = StringVar(root)
seconds = StringVar(root)

hours_list = [str(i).zfill(2) for i in range(24)]
minutes_list = [str(i).zfill(2) for i in range(60)]
seconds_list = [str(i).zfill(2) for i in range(60)]

hours_menu = OptionMenu(frame, hours, *hours_list)
minutes_menu = OptionMenu(frame, minutes, *minutes_list)
seconds_menu = OptionMenu(frame, seconds, *seconds_list)

Label(frame, text="Hour").grid(row=1, column=1)
Label(frame, text="Minute").grid(row=1, column=2)
Label(frame, text="Second").grid(row=1, column=3)

hours_menu.grid(row=2, column=1)
minutes_menu.grid(row=2, column=2)
seconds_menu.grid(row=2, column=3)

# Add Button to set the alarm
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
