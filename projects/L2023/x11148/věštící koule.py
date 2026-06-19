from microbit import *
import random
odpovědi = [
    "ANO",
    "NE",
    "MOZNA",
    "NEJSPIS",
    "ASI",
    "NEKDY V BUDOUCNU",
    "JESTE JEDNOU",
]
while True:
    if accelerometer.was_gesture('shake'):
        sleep(1000)
        vyber= random.choice(odpovědi)
        display.scroll (vyber)
        sleep(1000)