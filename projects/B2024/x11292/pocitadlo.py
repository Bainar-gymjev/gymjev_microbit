# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever

pocet = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
         pocet = 0
         display.scroll("0")
    elif button_a.was_pressed():
         pocet +=1
         display.scroll(str(pocet))
    elif button_b.was_pressed():
         pocet -=1
         display.scroll(str(pocet))