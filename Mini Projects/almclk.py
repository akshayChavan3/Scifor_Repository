import pygame
import datetime
import time

def alarm(hour, minute, second):
    set_alarm_time = f"{hour:12}:{minute:30}:{second:0}"

    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\sures\Downloads\alarm.mp3")  # Use a raw string (r"") or double backslashes
    pygame.mixer.music.play()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time:
            print("Time to Wake up")
            pygame.mixer.music.stop()
            break

        time.sleep(1)

# Example usage:
alarm(12, 30, 0)  # Replace with your desired time


