# Imports go at the top
from microbit import *
import music


# Code in a 'while True:' loop repeats forever
while True:
    if pin_logo.is_touched():
        display.show(Image('00300:'
                           '03630:'
                           '36963:'
                           '03630:'
                           '00300'))
        music.set_tempo(bpm=40)
        music.play(['E4:1','E4:1','E4:2','E4:1','E4:1','E4:2','E4:2','G4:1','C4:1','D4:1','E4:1','R:2','F4:1','F4:1','F4:1','F4:1','F4:1','E4:1','E4:1','E4:1','E4:1','D4:1','D4:1','E4:1','D4:2','G4:2'])
        display.scroll( 'Vanoce jsou za rohem')
        
       

        
