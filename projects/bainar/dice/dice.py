from microbit import *
import random 


dice = Image('55555:'
             '59095:'
             '50905:'
             '59095:'
             '55555:'
            )

display.show(dice)
while True:
    if accelerometer.was_gesture('shake'):
        for _ in range(50):
            display.show(random.randint(1, 6))
            sleep(75)
            