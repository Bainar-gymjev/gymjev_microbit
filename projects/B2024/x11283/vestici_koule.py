from microbit import *
import random
odpovedi = [Image.HAPPY, Image.SAD, Image.MEH]

while True:
    if accelerometer.is_gesture("shake"):
        display.clear()
        sleep(500)
        nahodna_volba = random.choice(odpovedi)
        display.show(nahodna_volba)