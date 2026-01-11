# Alarm clock

import datetime
import time
import pygame
def alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake Up 🥱")
            pygame.mixer.init()
            pygame.mixer.music.load("C:/Users/srir4/Downloads/samsung.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            break
        time.sleep(1)
if __name__ =="__main__":
    alarm_time = input("Enter the Alarm Time in (H:M:S) format: ")
    alarm(alarm_time)