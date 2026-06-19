# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.DUCK)
    sleep(1500)
    display.scroll('UNHAPPY or HAPPY?')
    if button_a.was_pressed():
        display.show(Image.SAD)
        sleep(1500)
        display.scroll("YOU GOT THE SAD FACE!!!")
    if button_b.was_pressed():
        display.show(Image.SMILE)
        sleep(1500)
        display.scroll("YOU GOT THE SMILEY FACE!!!")