from tkinter import *
import datetime
import time
import winsound
from threading import Thread


def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)


def set_alarm():
    Threading()


# Create the main window
root = Tk()
root.title("Alarm Clock")

# Create and pack labels
label = Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"))
label.pack(pady=20)

frame = Frame(root)
frame.pack()

# Optionmenus for hours, minutes, and seconds
hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set("06")
minutes.set("19")
seconds.set("05")

hour_menu = OptionMenu(frame, hours, *range(24))
minute_menu = OptionMenu(frame, minutes, *range(60))
second_menu = OptionMenu(frame, seconds, *range(60))

hour_menu.grid(row=1, column=1)
minute_menu.grid(row=1, column=2)
second_menu.grid(row=1, column=3)

Label(frame, text="Hours").grid(row=0, column=1)
Label(frame, text="Minutes").grid(row=0, column=2)
Label(frame, text="Seconds").grid(row=0, column=3)

# Create and pack set alarm button
set_button = Button(root, text="Set Alarm", font=("Helvetica", 14, "bold"), command=set_alarm)
set_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
